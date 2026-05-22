import requests

url = 'https://api.open-meteo.com/v1/forecast'


params = {
    "latitude": -20.3155,
    "longitude": -40.3128,
    "current": "temperature_2m,relative_humidity_2m",
    "timezone": "auto"
}

response = requests.get(url, params=params)
data = response.json()

temperature = data["current"]["temperature_2m"]
humidity = data["current"]["relative_humidity_2m"]

print("Weather in Vitória")
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")


