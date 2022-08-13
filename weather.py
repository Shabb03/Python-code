#!/usr/bin/env python3

#REFERENCE: https://www.youtube.com/watch?v=Oz3W-LKfafE&list=PLRwV8PM4b0OAOn-ayvzv4lNcbQyhovnFI&index=6

import requests

API_KEY = "be8fcd0b12d82802473ff59ea68698fc"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city:  ")
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "C")
else:
    print("Error!")