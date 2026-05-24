import requests


def get_weather_description(code):
    weather_codes = {
        0: "Céu limpo",
        1: "Predominantemente limpo",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Nevoeiro",
        48: "Nevoeiro congelante",
        51: "Garoa fraca",
        53: "Garoa",
        55: "Garoa forte",
        61: "Chuva fraca",
        63: "Chuva",
        65: "Chuva forte",
        80: "Pancadas de chuva fraca",
        81: "Pancadas de chuva",
        82: "Pancadas de chuva forte",
        95: "Tempestade",
    }

    return weather_codes.get(code, "Condição desconhecida")


def get_coordinates(city_name):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city_name,
        "count": 3,
        "language": "en",
        "format": "json",
    }

    response = requests.get(geo_url, params=geo_params)
    data = response.json()

    if "results" not in data:
        return None

    city = data["results"][0]

    return {
        "name": city["name"],
        "state": city.get("admin1", ""),
        "country": city["country"],
        "latitude": city["latitude"],
        "longitude": city["longitude"],
    }


def get_weather(latitude, longitude):
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code",
        "timezone": "auto",
    }

    response = requests.get(weather_url, params=weather_params)
    data = response.json()

    return data["current"]


print("=== Aplicativo de Clima v2 ===")

city_name = input("Digite a cidade: ").strip().replace("_", " ")

print("Buscando cidade...")
location = get_coordinates(city_name)

if location is None:
    print("Cidade não encontrada.")
    exit()

print("Buscando clima...")
weather = get_weather(location["latitude"], location["longitude"])

temperature = weather["temperature_2m"]
humidity = weather["relative_humidity_2m"]
feels_like = weather["apparent_temperature"]
weather_code = weather["weather_code"]

condition = get_weather_description(weather_code)

print()

if location["state"]:
    print(f"Clima em {location['name']}, {location['state']}, {location['country']}")
else:
    print(f"Clima em {location['name']}, {location['country']}")

print(f"Temperatura: {temperature}°C")
print(f"Sensação térmica: {feels_like}°C")
print(f"Umidade: {humidity}%")
print(f"Condição: {condition}")