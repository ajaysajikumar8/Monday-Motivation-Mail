import random
import smtplib
import datetime as dt


my_email = "ajaysajikumartest@yahoo.com"
password = "8LgqjMbZDAd#tM%"

#---------------------CHECK DATE------------------------#
now = dt.datetime.now()
day_of_the_week = now.weekday()

#---------------------FETCH RANDOM QOUTE------------------------#
with open("quotes.txt") as file:
    data = file.readlines()
    random_quote = random.choice(data)
    print(random_quote)

#---------------------EMAIL LOGIC------------------------#
if day_of_the_week == 0:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user= my_email, password= password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ajaysajikumartest@google.com", 
            msg=random_quote
        )