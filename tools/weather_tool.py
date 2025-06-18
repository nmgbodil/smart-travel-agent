from dotenv import load_dotenv

import requests
import os

load_dotenv()

OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')

def get_weather(city: str, timestamp: int) -> str:
    '''
    Get weather for a given city.

    Parameters
        city (str): Name of the city
        timestamp (int): Epoch Unix time of the day
    
    Returns

        weather_data (dict): Example below
                           
        {
            "lat": 52.2297,
            "lon": 21.0122,
            "timezone": "Europe/Warsaw",
            "timezone_offset": 3600,
            "data": [
                {
                    "dt": 1645888976,
                    "sunrise": 1645853361,
                    "sunset": 1645891727,
                    "temp": 279.13,
                    "feels_like": 276.44,
                    "pressure": 1029,
                    "humidity": 64,
                    "dew_point": 272.88,
                    "uvi": 0.06,
                    "clouds": 0,
                    "visibility": 10000,
                    "wind_speed": 3.6,
                    "wind_deg": 340,
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ]
                }
            ]
        }
                           
    '''
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={3}&appid={OPENWEATHER_API_KEY}")
    lat = response.content[0]["lat"]
    lon = response.content[0]["lon"]

    response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={OPENWEATHER_API_KEY}")

    return response.content