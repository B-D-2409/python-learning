# import smtplib
#
# my_email = "borislav.2404g@gmail.com"
# password = "cwybbmewaslpmxhx"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="borislav.davidov59@gmail.com",
#         msg="Subject:Hello\n\nThis is a test email."
#     )
#     connection.close()

# import datetime as dt
# from calendar import month
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# week_day = now.weekday()
#
#
# date_of_birth = dt.datetime(year=1995,month=12,day=15, hour=4)
# print(date_of_birth)


import smtplib
import datetime as dt
import random
my_email = "borislav.2404g@gmail.com"
password = "cwybbmewaslpmxhx"
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Monday Motivation\n\n{quote}")
