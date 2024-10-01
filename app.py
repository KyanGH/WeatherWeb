from flask import Flask, render_template
import requests


api_key = '96939010abda3f5161695ffe0efa2010'

user_input = input("Enter city: ")
print(user_input)

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

print(weather_data.status_code)
print(weather_data.json())

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    