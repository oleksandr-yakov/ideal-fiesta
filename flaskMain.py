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

	if response['cod'] == '404':
		error_message = f"Sorry, we couldn't find weather information for {city}. Please try again."
		return render_template('index.html', error=error_message)
	else:
		weather = {
			'city': city,
			'temperature': response['main']['temp'],
			'description': response['weather'][0]['description']
		}
		return render_template('index.html', weather=weather)


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # A database

        return 'User registered successfully!'
    else:
        return render_template('register.html')

if __name__ == '__main__':
	app.run(debug=True)