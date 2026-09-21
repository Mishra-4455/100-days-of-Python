import requests

api_key = "f4c4aa8f7bff31a173cfc48457f9c1fd"
OWM_api = "https://pro.openweathermap.org/data/2.5/forecast"

weather_paras = {
    "lat" : 22.619532750480353,
    "lon" : 88.32773655861286,
    "appid" : api_key,
    "exclude" : "current,minutely,daily"
}

Total_data = requests.get(OWM_api, params=weather_paras)
data = Total_data.json()
required_data = data["list"][:12]
rain = [True for i in required_data if i["weather"][0]["id"] < 700]

if True in rain:
    print("Be sure to bring an umbrella.")
# print(data["list"][0]["weather"][0])
# print(data)

