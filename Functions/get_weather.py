import requests
import json

#https://openweathermap.org/current#data

def get_weather():
    try:
        req = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=-23.3965&lon=-46.3214&appid=15f9bf5b8a2d6dc1eb5838460f531685&units=metric')
    except Exception as e:
        print('Error while requestion api')
        print(e)

    try:
        weather = json.loads(req.text)

        condition = weather['weather'][0]['description']
        temperature_now = weather['main']['temp']
        temperature_feel = weather['main']['feels_like']
        temperature_max = weather['main']['temp_max']
        temperature_min = weather['main']['temp_min']
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']
        clouds_percentage = weather['clouds']['all']
        place = weather['name']
    except Exception as e:
        print('Error while getting weather information from api')
        print(e)

    print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    print('┃','              ',place,'                  ┃')
    print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  ')
    print('┃ Weather condition: ', condition, '         ┃')
    print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  ')
    print('┃ Temperature: ', temperature_now, '°C', '                ┃')
    print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  ')
    print('┃ Feels like: ', temperature_feel, '°C', '                 ┃')
    print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  ')
    print('┃ Max temperature: ', temperature_max, '°C','            ┃')
    print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  ')
    print('┃ Min temperature: ', temperature_min, '°C', '            ┃')
    print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  ')
    print('┃ Humidity:', humidity, '%', '                        ┃')
    print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  ')
    print('┃ Wind speed: ', wind_speed, 'm/s                  ┃')
    print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  ')
    print('┃ Cloud coverage: ', clouds_percentage, '%                   ┃')
    print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  ')