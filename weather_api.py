import requests

API_KEY = "8b8fff71dc1e73a2b4521f8719032372"

def get_weather(city, country):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        return None

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    return temp, humidity, weather