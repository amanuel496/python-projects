import requests
from twilio.rest import Client

api_key = <api key> # Your "Open Weather Map" api key
MY_LAT = "8.541080"
MY_LONG = "39.269460"
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
twilio_account_sid = <account_sid> # Your twilio account sid
twilio_auth_token = <auth token> # Your twilio auth token

paramters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=paramters)
response.raise_for_status()

weather_data = response.json()
next_12hrs_weather = weather_data["hourly"][:12]
next_12hrs_weather_id = []
for i in range(len(next_12hrs_weather)):
    next_12hrs_weather_id.append(next_12hrs_weather[i]["weather"][0]["id"])

will_rain = False
for id in next_12hrs_weather_id:
    if id < 700:
        will_rain = True
        break

if will_rain:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_=<twilio virtual num>, # Your twilio provided virtual number
        to=<verified phone num> # Your twilio verified phone number
    )
    print(message.status)