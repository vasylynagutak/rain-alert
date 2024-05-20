import requests

import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_ACCOUNT_TOKEN = os.getenv("TWILIO_ACCOUNT_TOKEN")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "a0f6859a98013a5ff9d7aaa8b9b9ed42"

weather_params = {
    "lat": 45.872002,
    "lon": 17.845921,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = (response.json())

will_rain = False
condition_code = weather_data["weather"][0]["id"]
if int(condition_code) < 700:
    will_rain = True

if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_ACCOUNT_TOKEN)
    message = client.messages.create(
        body="It's going to rain.Bring an umbrella ☂️",
        from_="phone number",
        to="phone number"
    )
    print(message.status)