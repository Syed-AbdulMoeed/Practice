import time, requests, json
from threading import Thread, Lock
import matplotlib.pyplot as plt
import datetime

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
    end_date = datetime.date.today() - datetime.timedelta(days=1)  # yesterday (API may lag)
    start_date = end_date - datetime.timedelta(days=14)
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_mean",
    }

    response = requests.get(url, params=params, timeout=10)
    res = response.json()
    dates = res['daily']['time']
    temps = res['daily']['temperature_2m_mean']
    avg_temp = round(sum(temps)/len(temps), 3)
    data = {'dates' :dates,'temps' : temps, 'avg_temp' : avg_temp}
        
    
    with lock:
        old = read_data()
        if changed(data, old, name):
            write_data(data, name, old)
        else:
            print('no change')


def changed(data, old, name):
    return data != old[name]


# Write to File
def write_data(data, name, file_data) -> None:    
        
        if not file_data:
            print('error reading file')
            return
        file_data[name] = data
        with open('weather_data.json', 'w') as f:
            json.dump(file_data, f, indent=4)
    

# Read File Content
def read_data() -> dict:
    '''
    Reads data from the json file return a dict 
    '''    
    with open('weather_data.json', 'r') as f:
        return json.load(f)
    
        

    

def main():
    threads = []
    for city in CITIES:
        threads.append( Thread(target=get_weather_data, args=(city, CITIES[city]['lat'], CITIES[city]['lon'], API_BASE, LOCK)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('finished')
main()