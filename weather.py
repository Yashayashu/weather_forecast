import requests
import os
from datetime import datetime


user_api = os.environ.get('current_weather_data')

if not user_api:
    print("Error: OpenWeatherMap API key 'current_weather_data' not found in environment variables.")
else:
    location = input("Enter the city name: ")

    complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"

    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    if api_data.get('cod') == 404:
        print("Invalid city: {}, please check your city name".format(location))
    else:
        temp_city = (api_data['main']['temp'] - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_speed = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        print("-------------------------------------------------------------")
        print("Weather status for - {} || {}".format(location.upper(), date_time))
        print("-------------------------------------------------------------")
        print("Current temperature is: {:.2f} deg C".format(temp_city))
        print("Weather description: ", weather_desc)
        print("Current humidity: ", hmdt, '%')
        print("Current wind speed: ", wind_speed, 'kmph')
