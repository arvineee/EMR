from flask import  jsonify,request,render_template
import requests
import json
from datetime import datetime
from app import app



api_key = '33a892485ab4437faca121523251102'
base_url = 'http://api.weatherapi.com/v1/current.json'

def get_weather_data(city):
    url = f"{base_url}?key={api_key}&q={city}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        data = {
            "location": data['location']['name'],
            "region": data['location']['region'],
            "country": data['location']['country'],
            "temp_c": data['current']['temp_c'],
            "condition": data['current']['condition']['text'],
            "humidity": data['current']['humidity'],
            "wind_kph": data['current']['wind_kph'],
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


@app.route('/')
def index():
    city = request.args.get('city', '')  # Get the city from the form input
    weather_data = get_weather_data(city) if city else None
    return render_template('index.html', weather_data=weather_data)




