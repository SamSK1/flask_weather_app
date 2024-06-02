import os 
from dotenv import load_dotenv
from pprint import pprint
import requests

load_dotenv()
def get_current_weather(city='Zurich'):
    
    weather_api_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data=requests.get(weather_api_url).json()
    return weather_data

if __name__=="__main__":
    print("***entered weather module***")
    
    city=input(f"\nPlease enter city name: ")

    if type(city)==None:
        city='Zurich'
    elif bool(city.strip())==False:
        city='Zurich'
    weather_data=get_current_weather(city)
    
    print("****")
    pprint(weather_data)