import requests
from datetime import datetime

BASE_URL = "https://api.weather.example.com"


def fetch_weather_data(city):
    response = requests.get(f"{BASE_URL}/current", params={"city": city})
    response.raise_for_status()
    return response.json()


def fetch_forecast(city, days=3):
    response = requests.get(f"{BASE_URL}/forecast", params={"city": city, "days": days})
    response.raise_for_status()
    return response.json()


def get_current_hour():
    return datetime.now().hour
