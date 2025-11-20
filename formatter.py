import logging
from datetime import datetime

logging.basicConfig(
    filename='weather.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def format_weather(data, forecast_type):
    try:
        if forecast_type == "now":
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            city = data['name']
            return (
                f"🌤️ Погода в {city}:\n"
                f"🌡 Температура: {round(temp)}°C\n"
                f"☁️ {desc}"
            )
        
        elif forecast_type == "week":
            # Группируем прогнозы по дням
            daily_forecasts = {}
            for item in data['list']:
                dt_txt = item['dt_txt']
                # Извлекаем дату (без времени)
                date_str = dt_txt.split()[0]  # Формат: 'YYYY-MM-DD'
                if date_str not in daily_forecasts:
                    daily_forecasts[date_str] = {
                        'temp': item['main']['temp'],
                        'desc': item['weather'][0]['description']
                    }
            
            # Формируем итоговый текст
            result = "📅 Прогноз на неделю:\n"
            for date_str in sorted(daily_forecasts.keys()):
                temp = daily_forecasts[date_str]['temp']
                desc = daily_forecasts[date_str]['desc']
                # Преобразуем 'YYYY-MM-DD' в 'DD.MM'
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                formatted_date = date_obj.strftime('%d.%m')
                result += (
                    f"\n📅 {formatted_date}:\n"
                    f"🌡 Температура: {round(temp)}°C\n"
                    f"☁️ {desc}\n"
                )
            return result
        
        else:
            logging.error(f"Неизвестный тип прогноза: {forecast_type}")
            return "❌ Неверный тип прогноза"
    
    except KeyError as e:
        logging.error(f"Не удалось распарсить данные API. Отсутствует ключ: {e}")
        return "❌ Не удалось получить данные"
    except Exception as e:
        logging.error(f"Неожиданная ошибка: {type(e).__name__}: {e}")
        return "❌ Произошла ошибка при обработке данных"
