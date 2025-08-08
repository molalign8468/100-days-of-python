##################### Extra Hard Starting Project ######################
import random
import smtplib
import datetime as dt
import pandas

MY_EMAIL = "@gmail.com" # Update with your Email
PASSWORD=""#update with your Gmail App Password
SMTP_HOST="smtp.gmail.com"

# 2. Check if today matches a birthday in the birthdays.csv

data = pandas.read_csv("birthdays.csv")
birthdays =data.to_dict(orient="records")

now = dt.datetime.now()

for birthday in birthdays:
    random_index = random.randint(1,3)
    if now.month ==birthday["month"] and now.day == birthday["day"]:
        how_old = now.year - birthday["year"]
        with open(f"./letter_templates/letter_{random_index}.txt") as letter_file:
            letter_content = letter_file.read()
            mail_content = letter_content.replace("[NAME]",birthday["name"]).replace("[Year]",f"{how_old}")
            with smtplib.SMTP(SMTP_HOST) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL,password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=birthday["email"],
                                    msg=f"Subject: Birthday Wish \n\n {mail_content}")


        







