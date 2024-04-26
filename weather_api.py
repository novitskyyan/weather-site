import json
import datetime
import os

import requests
from dotenv import load_dotenv

load_dotenv()


class Weather:
    TOKEN = os.environ['TOKEN']
    LINK_1 = f"{os.environ['LINK']}/data/2.5/weather?q="
    LINK_2 = '&appid='
    LINK_3 = '&lang=ru'

    def __init__(self, city):
        self.city = city

    def get_info(self):
        info = requests.get(
            Weather.LINK_1 + self.city + Weather.LINK_2 + Weather.TOKEN + Weather.LINK_3).text
        info_dict = json.loads(info)
        min_temp = info_dict['main']['temp_min'] - 273
        max_temp = info_dict['main']['temp_max'] - 273
        temp = info_dict['main']['temp'] - 273
        description = info_dict['weather'][0]['description']
        wind = info_dict['wind']['speed']
        sunrise = info_dict['sys']['sunrise']
        sunset = info_dict['sys']['sunset']
        info = [
            f"{self.city}",
            f"Температура: {round(temp, 2)}",
            f"Минимальная температура: {round(min_temp, 2)}",
            f"Максимальная температура: {round(max_temp, 2)}",
            f"{description}",
            f"Скорость ветра: {wind} м/с",
            f"Рассвет: {datetime.datetime.utcfromtimestamp(sunrise).hour}",
            f"Закат: {datetime.datetime.utcfromtimestamp(sunset).hour}"]
        return info
