from flask import Flask, render_template, request
import requests, datetime, mysql.connector
from config import TOKEN

app = Flask(__name__)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='nuhayserver',
    database='prodMain'
)


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
        return render_template('synoptyk.html', error=error_message)
    else:
        weather = {
            'city': city,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['main'],
        }
        return render_template('synoptyk.html', weather=weather)

@app.route('/proweather', methods=['POST'])
def ProGet_weather():
    smiles = {
        "Clear": "\U00002600",
        "Clouds": "\U00002601",
        "Rain": "\U00002614",
        "Drizzle": "\U00002614",
        "Thunderstorm": "\U000026A1",
        "Snow": "\U0001F328",
        "Mist": "\U0001F32B",
        "Haze": "\U0001F32B"
    }
    city = request.form['city']

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={TOKEN}'

    response = requests.get(url).json()

    if response['cod'] == '404':
        error_message = f"Sorry, we couldn't find weather information for {city}. Please try again."
        return render_template('pro.html', error=error_message)
    else:
        weather = response['weather'][0]['main']
        if weather in smiles:
            smile = smiles[weather]
        weatherPro = {
            'city': city,
            'temperature': response['main']['temp'],
            'pro_description': response['weather'][0]['main']+f"{smile}"*3,
            'feels_like': response['main']['feels_like'],
            'speed': response['wind']['speed'],
            'humidity': response['main']['humidity'],
            'pressure': response['main']['pressure'],
            'sunrise': str(datetime.datetime.fromtimestamp(response['sys']['sunrise'])),
            'sunset': str(datetime.datetime.fromtimestamp(response['sys']['sunset'])),
            'bright_PartOfTheDay': str(datetime.datetime.fromtimestamp(
             response['sys']['sunset']) - datetime.datetime.fromtimestamp(response['sys']['sunrise']))
        }
        return render_template('pro.html', weatherPro=weatherPro)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor()
        query = "INSERT INTO usersdata (username, password) VALUES (%s, %s)"
        values = (username, password)
        cursor.execute(query, values)
        db.commit()

        return render_template('pro.html')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor()
        query = "SELECT * FROM usersdata WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            return render_template('pro.html')
        else:
            error_message = f"Sorry, but you entered the Invalid email or password"
            return render_template('login.html', errorlogin=error_message)

    return render_template('login.html')


@app.route('/synoptyk')
def synoptyk_for_user():
    return render_template('synoptyk.html')


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
