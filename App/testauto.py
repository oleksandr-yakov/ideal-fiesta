import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<p>Welcome to Weather Now, your go-to destination for up-to-the-minute weather updates in your city! "
                      b"We understand the importance of accurate and real-time weather information, and that's exactly what we provide. "
                      b"With Weather Now, you can instantly access the current weather conditions in your city, ensuring you stay prepared "
                      b"for whatever Mother Nature has in store for you. Whether you're planning your day, deciding what to wear, or simply "
                      b"curious about the weather outside, we've got you covered. Our user-friendly interface allows you to effortlessly navigate "
                      b"through the site and retrieve the most relevant weather data in just a few clicks. As soon as you land on Weather Now, you'll "
                      b"find a prominently displayed search bar where you can input your city name. In an instant, you'll be presented with the latest "
                      b"temperature, humidity, wind speed, and atmospheric conditions for your location. Our commitment to accuracy is unwavering. Weather "
                      b"Now sources data from reliable meteorological agencies and employs advanced forecasting algorithms to ensure you receive the most p"
                      b"recise weather information available. We understand the importance of timely updates, and our dedicated team works tirelessly to keep "
                      b"the data constantly refreshed. So, whether you're an outdoor enthusiast, a frequent traveler, or simply want to stay informed about t"
                      b"he weather in your city, Weather Now is your ultimate companion. Join us today and experience the power of real-time weather "
                      b"knowledge at your fingertips!</p>", response.data)
        print("index.html working and exists")
    def test_synoptyk(self):
        response = self.client.get('/synoptyk')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<input type="text" id="city" name="city" required>', response.data)
        print("synoptyk.html working and exists")
    def test_pro(self):
        response = self.client.get('/pro')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<label for="city">City:</label>', response.data)
        print("pro.html working and exists")

    def test_invalid_city(self):
        response = self.client.post('/weather', data={'city': 'fgfgjhj'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<p>Sorry, we couldn't find weather information for fgfgjhj</p>", response.data)
        print("Successfully Finnished test test_invalid_city ")

    def test_valid_city(self):
        response = self.client.post('/weather', data={'city': 'Paris'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Paris Weather</h2>', response.data)
        print("Successfully Finnished test test_valid_city ")

    def test_register(self):
        response = self.client.post('/register', data={'username': 'testuser', 'password': 'testpass', 'confirm_password': 'testpass'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<button type="submit">Get  ProWeather</button>', response.data)
        response = self.client.post('/login', data={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<button type="submit">Get  ProWeather</button>', response.data)
        print("Successfully Finnished test register and login")

if __name__ == '__main__':
    unittest.main()