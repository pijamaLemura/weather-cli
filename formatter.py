#formatter.py
import logging

logging.basicConfig(filename='weather.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def format_weather(data, forecast_type):
    try:
        if forecast_type == "now":
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            city = data['name']
            return f"🌤️ Погода в {city}:\n🌡 Температура: {round(temp)}°C\n☁️ {desc}"
        else:  # week
            # Для простоты пока выводим первый день
            day = data['list'][0]
            temp = day['main']['temp']
            desc = day['weather'][0]['description']
            dt = day['dt_txt']
            return f"📅 Прогноз на {dt}:\n🌡 Температура: {round(temp)}°C\n☁️ {desc}"
    except KeyError:
        logging.error("Не удалось распарсить данные API")
        return "❌ Не удалось получить данные"
