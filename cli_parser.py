# cli_parser.py
import click
from weather_api import get_weather
from formatter import format_weather
from cache_manager import get_cached_weather, set_cached_weather

@click.command()
@click.option('--city', prompt='Город', help='Название города')
@click.option('--forecast', type=click.Choice(['now', 'week']), default='now',
              help='Тип прогноза: сейчас или на неделю')
def main(city, forecast):
    forecast_type = "current" if forecast == "now" else "week"

    cached_data = get_cached_weather(city, forecast_type)
    if cached_data:
        print("✅ Взято из кэша")
        data = cached_data
    else:
        try:
            data = get_weather(city, forecast_type)
            set_cached_weather(city, forecast_type, data)
            print("✅ Запрос отправлен, результат сохранён в кэш")
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            return

    result = format_weather(data, forecast)
    print(result)

if __name__ == "__main__":
    main()
