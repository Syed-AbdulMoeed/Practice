import time, requests
import threading
import matplotlib.pyplot as plt

'''
------------------------------------------------
Structure
------------------------------------------------
get_weather_data
store -> csv
graph plot
emai burning acc results
host later
2 threads
1 thread gets weather data
1. Parallel City Data Pipelines
2. The "Heavy Lifter" (Plotting and Reporting)
3. Process for writing to disk

1 function for each city

'''

cities = {
    'Jeddah': {'lat': 21.5433, 'lon': 39.1728},
    'Lahore': {'lat': 31.5204, 'lon': 74.3587},
    'Deggendorf': {'lat': 48.8354, 'lon': 12.9644},
}

API_BASE = "https://archive-api.open-meteo.com/v1/archive"

def get_weather(name, lat, lon, url):
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": "2026-04-29",
        "end_date": "2026-05-13",
        "daily": "temperature_2m_mean",
    }

    response = requests.get(url, params=params)
    res = response.json()
    dates = res['daily']['time']
    temps = res['daily']['temperature_2m_mean']
    
    

get_weather('Jeddah', cities['Jeddah']['lat'], cities['Jeddah']['lon'], API_BASE)