import requests
from datetime import datetime
import smtplib

MY_LAT = 22.57688 # Your latitude
MY_LONG = 88.31857 # Your longitude
my_email= "pythontest1112011@gmail.com"
my_password= "tzxsyatzwjbvrpek"

#Your position is within +5 or -5 degrees of the ISS position.
def check_iss_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude-5 <= MY_LAT <=iss_latitude+5 and iss_longitude-5 <= MY_LONG <=iss_longitude+5

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

if (time_now >= sunset or time_now <= sunrise) and check_iss_pos():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:ISS AHEAD!!\n\nLOOK UP THERE IS THE INTERNATIONAL SPACE STATION GOING ABOVE YOU RIGHT NOW"
    )
else:
    print("There is no ISS above your location right now.")