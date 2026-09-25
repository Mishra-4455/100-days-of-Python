import requests
import smtplib
import os
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_vals = []

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.

or

"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

stock_api = "https://www.alphavantage.co/query"
news_api = "https://newsapi.org/v2/everything"
my_email= "pythontest1112011@gmail.com"
my_password= os.environ.get("PY_EMAIL_PASSWORD")

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : os.environ.get("STOCK_API")
}

Time = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

news_params = {
    "q" : "tesla",
    "from" : Time,
    "sortBy" : "publishedAt",
    "apiKey" : os.environ.get("NEWS_API"),
    "language" : "en"
}

stock_obj = requests.get(stock_api, params=stock_params)
stock_obj.raise_for_status()
print(stock_obj.status_code)
stock_data_full = stock_obj.json()
twoEntry = dict(list(stock_data_full["Time Series (Daily)"].items())[:2])
for key,value in twoEntry.items():
    stock_vals.append(float(value['4. close']))
diff = ((stock_vals[0] - stock_vals[1]) / stock_vals[1])*100

change = f"{abs(diff):.2f}%"
if (diff >= 5):
    change = f"🔺{diff:.2f}%"    
    news_obj = requests.get(news_api, params=news_params)
    news_obj.raise_for_status()
    print(news_obj.status_code)
    news_data_full = news_obj.json()
    news = news_data_full["articles"][:3]

    message = f"STOCK EXCHANGE\nTSLA: {change}\nNews:"
    for i in range(3):
        message += f"\n{i+1}. Headline: {news[i]["title"]}\nBrief: {news[i]["description"]}\n"
    print(message)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pythontest1112011@yahoo.com",
            msg=message
        )
    print("QUEUED")

elif (diff <= -5):
    change = f"🔻{abs(diff):.2f}%"
    news_obj = requests.get(news_api, params=news_params)
    news_obj.raise_for_status()
    print(news_obj.status_code)
    news_data_full = news_obj.json()
    news = news_data_full["articles"][:3]

    message = f"STOCK EXCHANGE\nTSLA: {change}\nNews:"
    for i in range(3):
        message += f"\n{i+1}. Headline: {news[i]["title"]}\nBrief: {news[i]["description"]}\n"
    print(message)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pythontest1112011@yahoo.com",
            msg=message
        )
    print("QUEUED")

else:
    print("Change is not greater than 5%, so the email was not sent.")