##################### Extra Hard Starting Project ######################
import smtplib
import pandas
import datetime as dt

# 1. Read the birthdays.csv
data = pandas.read_csv("birthdays.csv")

my_email = "borislav.2404g@gmail.com"
password = "cwybbmewaslpmxhx"

# Get today's date
now = dt.datetime.now()

for index, row in data.iterrows():
    # If there are still any empty date fields, skip the row (optional safety)
    if pandas.isna(row.year) or pandas.isna(row.month) or pandas.isna(row.day):
        continue

    birthday = dt.datetime(int(row.year), int(row.month), int(row.day))

    # 2. Check if today matches this person's birthday (only month & day)
    if birthday.month == now.month and birthday.day == now.day:
        # 3. Read the letter template and personalize it
        with open("letter_templates/letter_1.txt") as wishes_file:
            wishes = wishes_file.read().strip()
            wishes = wishes.replace("[NAME]", row["name"])

        # 4. Send the email
        email = str(row["email"]).strip()

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!\n\n{wishes}"
            )
