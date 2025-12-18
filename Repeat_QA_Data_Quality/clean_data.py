import os
import pandas as pd

RAW_FILE = "master_data_soda.csv"
CLEAN_FILE = "clean_master_data.csv"
SUMMARY_FILE = "cleaning_summary.csv"

CHUNK_SIZE = 10000


def main():
    # --- Reference / mapping tables (small, can be in-memory) ---
    vendor_data = pd.DataFrame({
        "Vendor_Code": ["V001", "V002", "V003"],
        "Vendor_Name": ["Coca-Cola Hellenic", "Glass Bottle Co.", "Sugar Refinery"]
    })

    category_map = {
        "Beverages": "BEV_01",
        "Snacks": "SNK_01",
        "Alcohol": "ALC_01",
        "Merchandise": "MER_01",
        "Raw Material": "RAW_01",
    }

    # --- Summary counters ---
    summary = {
        "rows_read": 0,
        "rows_written": 0,
        "dropped_negative_price": 0,
        "dropped_negative_stock": 0,
        "dropped_duplicate_id": 0,
        "filled_missing_active_status": 0,
        "unknown_vendor_marked": 0,
        "unmapped_category_marked": 0,
        "parsed_last_updated_to_datetime": 0,
    }

    # ============================================================
    # PASS 1: Find duplicates across the whole file (all chunks)
    # ============================================================
    id_counts = {}

    for chunk in pd.read_csv(RAW_FILE, chunksize=CHUNK_SIZE):
        # count IDs in this chunk
        vc = chunk["Material_ID"].value_counts(dropna=False)
        for k, v in vc.items():
            id_counts[k] = id_counts.get(k, 0) + int(v)

    duplicate_ids = {mid for mid, cnt in id_counts.items() if cnt > 1}

    # ============================================================
    # PASS 2: Clean + Enrich + Map, write output incrementally
    # ============================================================
    # Ensure we overwrite old output
    if os.path.exists(CLEAN_FILE):
        os.remove(CLEAN_FILE)

    seen_ids = set()
    wrote_header = False

    for chunk in pd.read_csv(RAW_FILE, chunksize=CHUNK_SIZE):
        summary["rows_read"] += len(chunk)

        # 1) Type fix: Last_Updated -> datetime (best effort)
        if "Last_Updated" in chunk.columns:
            before_na = chunk["Last_Updated"].isna().sum()
            chunk["Last_Updated"] = pd.to_datetime(chunk["Last_Updated"], errors="coerce")
            after_na = chunk["Last_Updated"].isna().sum()
            # if parsing created extra NaTs, we count those as "parse issues" (optional metric)
            summary["parsed_last_updated_to_datetime"] += max(0, int(after_na - before_na))

        # 2) Drop negative price
        mask_neg_price = chunk["Unit_Price"] < 0
        summary["dropped_negative_price"] += int(mask_neg_price.sum())
        chunk = chunk[~mask_neg_price].copy()

        # 3) Drop negative stock
        mask_neg_stock = chunk["Stock_Quantity"] < 0
        summary["dropped_negative_stock"] += int(mask_neg_stock.sum())
        chunk = chunk[~mask_neg_stock].copy()

        # 4) Handle duplicates: keep FIRST occurrence globally
        #    (including duplicates that occur in other chunks)
        if duplicate_ids:
            # First remove rows whose Material_ID is in duplicate_ids BUT we keep the first one we encounter
            # Strategy:
            # - if ID is not duplicate -> keep
            # - if ID is duplicate:
            #     - keep only if not seen_ids yet
            #     - otherwise drop
            keep_rows = []
            dropped_dups_here = 0

            for mid in chunk["Material_ID"].tolist():
                if mid in duplicate_ids:
                    if mid in seen_ids:
                        keep_rows.append(False)
                        dropped_dups_here += 1
                    else:
                        keep_rows.append(True)
                        seen_ids.add(mid)
                else:
                    keep_rows.append(True)
                    # track non-dup IDs too so if they appear later unexpectedly, we can still keep first
                    # (optional, but safe)
                    if mid in seen_ids:
                        # This would mean it became a dup; but pass1 already computed dups.
                        # We'll still drop later occurrences if it happens.
                        pass
                    else:
                        seen_ids.add(mid)

            summary["dropped_duplicate_id"] += dropped_dups_here
            chunk = chunk[pd.Series(keep_rows, index=chunk.index)].copy()
        else:
            # If no duplicates at all, still track seen to be safe
            for mid in chunk["Material_ID"].tolist():
                if mid not in seen_ids:
                    seen_ids.add(mid)

        # 5) Fill missing Active_Status -> 'N' (example approved rule)
        if "Active_Status" in chunk.columns:
            missing_active = int(chunk["Active_Status"].isna().sum())
            summary["filled_missing_active_status"] += missing_active
            chunk["Active_Status"] = chunk["Active_Status"].fillna("N")

        # 6) Vendor enrichment (LEFT JOIN)
        chunk = pd.merge(chunk, vendor_data, on="Vendor_Code", how="left")

        # Mark unknown vendors
        unknown_vendor = int(chunk["Vendor_Name"].isna().sum())
        summary["unknown_vendor_marked"] += unknown_vendor
        chunk["Vendor_Name"] = chunk["Vendor_Name"].fillna("UNKNOWN")

        # 7) Category -> SAP code mapping
        chunk["SAP_Category_Code"] = chunk["Category"].map(category_map)
        unmapped = int(chunk["SAP_Category_Code"].isna().sum())
        summary["unmapped_category_marked"] += unmapped
        chunk["SAP_Category_Code"] = chunk["SAP_Category_Code"].fillna("UNK_00")

        # 8) Append to output CSV
        chunk.to_csv(
            CLEAN_FILE,
            mode="a",
            index=False,
            header=(not wrote_header)
        )
        wrote_header = True
        summary["rows_written"] += len(chunk)

    # ============================================================
    # Export summary
    # ============================================================
    summary_df = pd.DataFrame([summary])
    summary_df.to_csv(SUMMARY_FILE, index=False)

    print("\n=== CLEANING DONE (CHUNK MODE) ===")
    print(f"Raw file:   {RAW_FILE}")
    print(f"Clean file: {CLEAN_FILE}")
    print(f"Summary:    {SUMMARY_FILE}")
    print("\nSummary counters:")
    print(summary_df.to_string(index=False))


if __name__ == "__main__":
    main()
