import os 
from dotenv import load_dotenv
import random
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
def get_random_weather():
    countries_api=requests.get('https://countriesnow.space/api/v0.1/countries').json()
    get_country_code=int(random.randint(0,len(countries_api['data'])-1))
    get_country=countries_api['data'][get_country_code]['country']
    get_city=random.choice(countries_api['data'][get_country_code]['cities'])

    weather_api_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={get_city}&units=metric'
    weather_data=requests.get(weather_api_url).json()
    return weather_data
if __name__=="__main__":
    print("***entered weather module***")
    
    get_random_weather()
    
    print("****")
