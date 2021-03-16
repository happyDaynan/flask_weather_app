import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    



@app.route('/')
def index():
    city_name = 'Las Vegas'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    r = requests.get(url).json()

    weather_data = []
    weather = {
        'city': city_name,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }
    
    weather_data.append(weather)
    
    
    
    return render_template('weather.html', weather_data=weather_data)

