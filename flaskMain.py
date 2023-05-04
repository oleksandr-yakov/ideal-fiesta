from flask import Flask, render_template, request, jsonify
import requests
from config import TOKEN

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/weather', methods=['POST'])
def get_weather():
	city = request.form['city']

	url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={TOKEN}'

	response = requests.get(url).json()


	if response['cod'] == 200:
		weather = {
			'city': city,
			'temperature': response['main']['temp'],
			'description': response['weather'][0]['description']
		}

		return render_template('index.html', weather=weather)
	else:
		return jsonify({'error': 'City not found'}), 404

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


if __name__ == '__main__':
	app.run(debug=True)