import smtplib

my_email = "borislav.2404g@gmail.com"
password = "cwybbmewaslpmxhx"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="borislav.davidov59@gmail.com",
        msg="Subject:Hello\n\nThis is a test email."
    )
    connection.close()
