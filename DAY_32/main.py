import smtplib
import datetime as dt
import random

my_email= "pythontest1112011@gmail.com"
my_password= "tzxsyatzwjbvrpek"
now = dt.datetime.now()
# year = now.year
# month = now.month
day_of_week = now.weekday()
# print(month)

with open("quotes.txt") as file:
    data = file.read()
    data_list = data.split("\n")
quote = random.choice(data_list)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="pythontest1112011@yahoo.com",
        msg=f"Subject:Motivational quote for day{day_of_week} of the week\n\n{quote}"
    )
