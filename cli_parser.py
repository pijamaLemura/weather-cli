# cli_parser.py
import click

@click.command()
@click.option('--city', prompt='Город', help='Название города')
@click.option('--forecast', type=click.Choice(['now', 'week']), default='now',
              help='Тип прогноза: сейчас или на неделю')
def main(city, forecast):
    """Запуск погодного клиента"""
    from weather_api import get_weather
    from formatter import format_weather

    try:
        data = get_weather(city, forecast)
        print(format_weather(data, forecast))
    except Exception as e:
        print(f"❌ Ошибка: {e}")
