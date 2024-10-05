from flask import Flask, render_template
import requests


api_key = '96939010abda3f5161695ffe0efa2010'





while(1):
    user_input = input("Enter city: ")
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
    weather = weather_data.json()['weather'][0]['main']
    weather_icon = weather_description = weather_data.json()['weather'][0]['icon']
    country = weather_data.json()['sys']['country']
    temp = (weather_data.json()['main']['temp'] - 32) * 5 / 9
    lon = weather_data.json()['coord']['lon']
    lat = weather_data.json()['coord']['lat']

    print(user_input)
    print(f"Weather: {weather}, Temperature: {temp:.2f}\u00B0C")
    print(f"Coordinates:\nLongtitude: {lon}")
    print(f"Icon: {weather_icon}")
    print(f"Country: {country}")
    print(weather_data.json())

# print(weather_data.status_code)
# print(weather_data.json())

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    