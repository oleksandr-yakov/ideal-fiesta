import requests
import datetime, pytz
from config import TOKEN, TG_TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def startBot(message: types.Message):
    userFULL = message.from_user.full_name
    await message.reply(f" Hi, {userFULL}!\n"
                        f"Please enter the city whose weather you want to know\n"
                        f"NEW UPDATE\n"
                        f"Type '/time' to see the Current Time in Kyiv and Ontario:\n"
                        )
    #user_id = message.from_user.id


@dp.message_handler(commands=["help"])
async def startBot(message: types.Message):
    userFULL = message.from_user.full_name
    await message.reply(f" Hi, {userFULL}!\n"
                        f"Type '/time' - current time Kyiv-Ontario\n"
                        f"Enter the city name like: 'Kyiv' 'Київ' \n"
                        )


@dp.message_handler(text=["JNK"])
async def startBot(message: types.Message):
    await message.reply(f"Returns TRUE!!! \U0001FAE1\n\n"
                        f"Support  - > Type '/help'\U0001FAE1\n")


@dp.message_handler(text=['/time'])
async def send_time(message: types.Message):
    kyiv_tz = pytz.timezone('Europe/Kiev')
    ontario_tz = pytz.timezone('Canada/Eastern')
    kyiv_time = pytz.datetime.datetime.now(kyiv_tz)
    canada_time = pytz.datetime.datetime.now(ontario_tz)
    response_text = f"Current time in Kyiv: {kyiv_time.strftime('%H:%M')}\nCurrent time in Ontario: {canada_time.strftime('%H:%M')}\n\nSupport  - > Type '/help'\U0001FAE1\n"
    await bot.send_message(chat_id=message.chat.id, text=response_text)


@dp.message_handler()
async def get_weather(message: types.Message):
    smileUpdate = {
        "Clear": "\U00002600",
        "Clouds": "\U00002601",
        "Rain": "\U00002614",
        "Drizzle": "\U00002614",
        "Thunderstorm": "\U000026A1",
        "Snow": "\U0001F328",
        "Mist": "\U0001F32B",
        "Haze": "\U0001F32B"
    }
    try:
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={TOKEN}&units=metric&lang=ru" # chosse the language - > add the  "&lang=ua"

        )
        OutputData = req.json()
        area = OutputData['sys']['country']
        CityName = OutputData['name']
        temp = OutputData['main']['temp']
        feels = OutputData['main']['feels_like']
        speed_wind = OutputData['wind']['speed']
        humidity = OutputData['main']['humidity']
        pressure = OutputData['main']['pressure']
        weather = OutputData['weather'][0]['main']
        if weather in smileUpdate:
            smiles = smileUpdate[weather]
        else:
            smiles = "Press F to pay respect \U0001FAE1 \U0001FAE1 \U0001FAE1"
        sunrise = datetime.datetime.fromtimestamp(OutputData['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(OutputData['sys']['sunset'])
        bright_PartOfTheDay = datetime.datetime.fromtimestamp(OutputData['sys']['sunset']) - datetime.datetime.fromtimestamp(OutputData['sys']['sunrise'])

        #print(f"Current time {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
        #f" Current time {time.asctime()}\n
        await message.reply(f"Current time {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
              f"City - > {CityName};  Сountry - > {area};\n"
              f"Shortly - > {weather} {smiles};\nTemperature - > {temp} °C;\n"
              f"Temperature Feels Like - > {feels}°C;\nSpeed of Wind - > {speed_wind} mps;\n"
              f"Humidity - > {humidity}%;\nPressure - > {pressure*0.750062} mmHg;\n"
              f"Sunrise - > {sunrise};\nSunset - > {sunset};\n"
              f"Bright Part Of The Day - > {bright_PartOfTheDay};\n\n"
              f"Support  - > Type '/help'\U0001FAE1\n")




    except:
        await message.reply("Check city name\nAnd enter the correct city name like: 'Kyiv' 'Київ'\n\nSupport  - > Type '/help'\U0001FAE1\n")



if __name__ == '__main__':
    executor.start_polling(dp)
