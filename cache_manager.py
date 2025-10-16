 #### ✅ Участник Рамзин М.А. : `cache_manager.py` + сборка

```python
# cache_manager.py
import json
import os
import time

CACHE_FILE = "weather_cache.json"
CACHE_TTL = 3600  # 1 час

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

def get_cached_weather(city, forecast_type):
    cache = load_cache()
    key = f"{city}_{forecast_type}"
    if key in cache:
        if time.time() - cache[key]['timestamp'] < CACHE_TTL:
            return cache[key]['data']
    return None

def set_cached_weather(city, forecast_type, data):
    cache = load_cache()
    key = f"{city}_{forecast_type}"
    cache[key] = {
        'timestamp': time.time(),
        'data': data
    }
    save_cache(cache)
