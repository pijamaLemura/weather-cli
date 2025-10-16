# weather_api.py
import requests
import json
from config import API_KEY

#API_KEY = "наш_ключ"  # лучше вынести в config.py

def get_weather(city, forecast_type="current"):
    base_url = "http://api.openweathermap.org/data/2.5/"
    if forecast_type == "now":
        url = f"{base_url}weather?q={city}&appid={API_KEY}&units=metric"
    elif forecast_type == "week":
        url = f"{base_url}forecast?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Ошибка при запросе погоды: {e}")
