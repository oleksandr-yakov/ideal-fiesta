import mysql.connector

TOKEN="999c8650aaa887b067488e5b7537917e"

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='nuhayserver',
    database='prodMain'
)

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