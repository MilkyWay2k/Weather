import eel
from pyowm import OWM
from pyowm.utils import config as cfg

config = cfg.get_default_config()
config['language'] = 'ru'

owm = OWM('d281d254f79245b469d342de46b2a62f', config)

@eel.expose
def get_weather(place):

    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    speed = w.wind()['speed']

    return "В " + place + " сейчас " + w.detailed_status + " ,температура в районе " + str(temp) + " градусов по Цельсию. Скорость ветра " + str(speed) + ", а влажность " + str(w.humidity) + "%!" 

eel.init("D:\Python\web")

eel.start("main.html", size=(700,700))