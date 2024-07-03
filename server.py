from flask import Flask, render_template, request
from my_weather_module import get_current_weather
from my_weather_module import get_weather_picture
from my_weather_module import get_random_weather
from waitress import serve
import pycountry_convert as pc

import webbrowser
import random
app=Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/base')
def index():
    return render_template('base.html')

@app.route('/weather')
def get_weather():
    city=request.args.get('city1')
    # if type(city)==None:
    #     city='Zurich'
        
    if bool(city.strip())==False:
        city='Zurich'
        
    weather_data=get_current_weather(city)
   
    if  weather_data['cod']!=200:
        weather_data=get_current_weather(city)
        return render_template('city_not_found.html')
    weather_data=get_current_weather(city)
    weather_picture=get_weather_picture(city)
    


    return render_template(
        "weather.html",
        title=str(weather_data['name']),
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        image=weather_picture

    )

@app.route('/random_weather')
def get_random_weather_city():

    
    
    try:
            
            weather_data=get_random_weather()
            city=weather_data['name']
    except:
            emergency_city=['Paris','London','Chur','Bologna','Hamburg','Bratislava','Lisabon','Moscow','Bangkok','Chiang Mai','Beijing','Johannesburg','Istanbul','Manchester']
            city=random.choice(emergency_city)

    # country_alpha2=weather_data['sys']['country']
    weather_data=None
    while weather_data==None or 'sys' not  in weather_data.keys():
         weather_data=get_random_weather()
    
    weather_data=get_current_weather(city)
    weather_picture=get_weather_picture(city)
    
    if 'name' not in weather_data or 'main' not in weather_data:
         return render_template('city_not_found.html')
    
    return render_template(        
        "weather.html",
        title=str(weather_data['name']),
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        image=weather_picture)
if __name__=="__main__":
    serve(app,host="0.0.0.0", port=5000)
    # app.run(debug=True,port=5000, host='0.0.0.0')