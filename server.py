from flask import Flask, render_template, request
from my_weather_module import get_current_weather
from my_weather_module import get_weather_picture
from waitress import serve
import webbrowser

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
        title=weather_data['name'],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        image=weather_picture

    )
if __name__=="__main__":
    # serve(app, port=8000)
    app.run(debug=True,port=5000, host='0.0.0.0')