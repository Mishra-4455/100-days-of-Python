import smtplib
import datetime as dt
import pandas
import random

my_email= "pythontest1112011@gmail.com"
my_password= "tzxsyatzwjbvrpek"
now = dt.datetime.now()
date = (now.month, now.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data['month'].item(), data['day'].item()):data for (index, data_row) in data.iterrows()}

if date in birthdays_dict:
    with open(f"letter_{random.randint(1,3)}.txt") as letter:
        letter_data = letter.read()
        final_letter = letter_data.replace("[NAME]", birthdays_dict[date]["name"].item())
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Happy Birthday!!!\n\n{final_letter}"
            )
            