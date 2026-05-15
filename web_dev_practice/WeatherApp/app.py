import time, requests, json
from threading import Thread, Lock
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
# Constants
CITIES = {
    'Jeddah': {'lat': 21.5433, 'lon': 39.1728},
    'Lahore': {'lat': 31.5204, 'lon': 74.3587},
    'Deggendorf': {'lat': 48.8354, 'lon': 12.9644},
}

API_BASE = "https://archive-api.open-meteo.com/v1/archive"

LOCK = Lock()

# Get Weather Data from API
def get_weather_data(name, lat, lon, url, lock):
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
    avg_temp = round(sum(temps)/len(temps), 3)
    data = {
        'name': name, 'dates':dates,'temps' : temps, 'avg_temp' : avg_temp
        }
    with lock:
        write_data(data)


# Write to File
def write_data(data) -> None:
    try:
        with open('weather_data.json', 'w') as f:
            json.dump(data, f, indent=4)
    except Exception:
        print('Error writing File')

# Read File Content
def read_data() -> dict:
    '''
    Reads data from the json file return a dict 
    '''
    try:
        with open('weather_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Error reading File')

    

def main():
    global CITIES, API_BASE, LOCK
    threads = []
    for city in CITIES:
        threads.append( Thread(target=get_weather_data, args=(city, CITIES[city]['lat'], CITIES[city]['lon'], API_BASE, LOCK)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('finished')
main()    