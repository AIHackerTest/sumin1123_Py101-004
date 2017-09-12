#! python3

from flask import Flask, render_template, request
import requests

list = []

def weather(name):
    url = 'https://api.seniverse.com/v3/weather/now.json'
    param = {'key': 'ghc8nixp7a89p9qk', 'location': name}
    dict = requests.get(url, params = param).json()
    a = dict['results'][0]['now']['text']
    b = dict['results'][0]['now']['wind_direction']
    c = dict['results'][0]['now']['temperature']
    weather_l = name + '的天气为' + a + ',风向为' + b + ',温度为' + c + '摄氏度.'
    return weather_l

app = Flask(__name__)

@app.route('/')
def index():
    try:
        if request.args.get('help') == 'Help':
            return render_template('help.html')
        elif request.args.get('query') == 'Query':
            x = request.args.get('city')
            display = weather(x)
            list.append(display)
            return render_template('query.html', w = display)
        elif request.args.get('history') == 'History':
            return render_template('history.html', list = list )
        else:
            pass
    except KeyError:
        return render_template('404.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
