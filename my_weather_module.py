import os 
from dotenv import load_dotenv

import requests

load_dotenv()
def get_current_weather(city='Zurich'):
    
    weather_api_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data=requests.get(weather_api_url).json()
    
    return weather_data
def get_weather_picture(city='Zurich'):
    get_weather_data=get_current_weather(city)
    icon_code=get_weather_data["weather"][0]['icon']
    
    image_url=f'https://openweathermap.org/img/wn/{icon_code}@2x.png'
    return image_url
if __name__=="__main__":
    print("***entered weather module***")
    
    city=input(f"\nPlease enter city name: ")

    if type(city)==None:
        city='Zurich'
    elif bool(city.strip())==False:
        city='Zurich'
    # weather_data=get_current_weather(city)
    print(get_weather_picture(city))
    
    print("****")
