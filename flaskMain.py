from flask import Flask, render_template, request
import requests
import datetime
from config import TOKEN

# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
# 	if request.method == 'POST':
# 		data = request.form['city']
# 		url = f'http://api.openweathermap.org/data/2.5/weather?q={data}&units=metric&appid={TOKEN}'
# 		OutputData = requests.get(url).json()
# 		if OutputData['cod'] == 200:
# 			area = OutputData['sys']['country']
# 			city = OutputData['name']
# 			temp = OutputData['main']['temp']
# 			feels = OutputData['main']['feels_like']
# 			speed_wind = OutputData['wind']['speed']
# 			humidity = OutputData['main']['humidity']
# 			pressure = OutputData['main']['pressure']
# 			weather = OutputData['weather'][0]['main']
# 			sunrise = str(datetime.datetime.fromtimestamp(OutputData['sys']['sunrise']))
# 			sunset = str(datetime.datetime.fromtimestamp(OutputData['sys']['sunset']))
# 			bright_PartOfTheDay = str(datetime.datetime.fromtimestamp(
# 				OutputData['sys']['sunset']) - datetime.datetime.fromtimestamp(
# 				OutputData['sys']['sunrise']))
# 			return {'City - >': city, 'Area - >': area, 'Temperature - >': temp, 'Temperature Feels Like - >': feels,
# 					'Speed of Wind - >': speed_wind, 'Humidity - >': humidity, 'Pressure - >': pressure * 0.750062,
# 					 'Sunrise - >': sunrise, 'Sunset - >': sunset, 'Bright Part Of The Day - >': bright_PartOfTheDay,'Weather': weather}
# 		else:
# 			return {'error': 'City not found'}
# 	return render_template("index.html")
#
#
# if __name__ == '__main__':
# 	app.run(debug=True)
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/weather', methods=['POST'])
def get_weather():
	city = request.form['city']

	url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={TOKEN}'

	response = requests.get(url).json()

	weather = {
		'city': city,
		'temperature': response['main']['temp'],
		'description': response['weather'][0]['description']
	}

	return render_template('index.html', weather=weather)


if __name__ == '__main__':
	app.run(debug=True)