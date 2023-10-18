import requests
from twilio.rest import Client

api_key = "1460a326b06906f175e99b679563040a"
account_sid = 'AC2117b51f874d6c08512bcecf36601b40'
auth_token = 'auth_token' #must be replaced

client= Client(account_sid, auth_token)

weather_params = {
    "lat": 44.318378,
    "lon": 23.796400,
    "appid": api_key

}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather", params=weather_params)
response.raise_for_status()
weather_code = response.json()["weather"][0]["id"]

if 500<= weather_code <=531:

    message = client.messages.create(
        from_='+17817677738',
        body=r"It's raining outside! You should bring an umbrella.",
        to = '+40761623757'
    )

    print(message.sid)
else:
    message = client.messages.create(
        from_='+17817677738',
        body=r"Clear sky!",
        to='+40761623757'
    )

    print(message.sid)
