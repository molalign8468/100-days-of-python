import smtplib
import datetime as dt
import random

MY_EMAIL = "hasetgetahun7@gmail.com"
PASSWORD = "" # Your Gmail App password 
SMTP_HOST="smtp.gmail.com"
TO_ADDRESS= "molalign229@gmail.com"

    
now = dt.datetime.now()
if now.weekday()==1:
    with smtplib.SMTP(SMTP_HOST) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)

        with open("quotes.txt") as file:
            file_list=file.readlines()
            random_quote=random.choice(file_list)
            quote = random_quote.split("-")
            quote_msg = quote[0]
            quote_by = quote[1]
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_ADDRESS,
                msg=f"Subject:Monday Motivation \n\n {quote_msg} \n by {quote_by}")

