#! python3
# coding: utf-8

import requests
from sys import exit
import time
from threading import Timer

def weather(city, type):
    url = 'https://api.seniverse.com/v3/weather/now.json'
    param = {'key': 'ghc8nixp7a89p9qk', 'location': city, 'unit': type}
    dict = requests.get(url, params = param).json()
    a = dict['results'][0]['now']['text']
    b = dict['results'][0]['now']['wind_direction']
    c = dict['results'][0]['now']['temperature']
    d = dict['results'][0]['last_update']
    time1 = d[0:10]
    time2 = d[11:16]
    list  = [a, b, c, time1, time2]
    return list
def weather_future(city, type, days):
    url = 'https://api.seniverse.com/v3/weather/daily.json'
    param = {'key': 'ghc8nixp7a89p9qk', 'location': city, 'unit': type}
    dict = requests.get(url, params = param).json()
    a = dict['results'][0]['daily'][days]['date']
    b = dict['results'][0]['daily'][days]['text_day']
    c = dict['results'][0]['daily'][days]['text_night']
    d = dict['results'][0]['daily'][days]['high']
    e = dict['results'][0]['daily'][days]['low']
    f = dict['results'][0]['daily'][days]['wind_direction']
    g = dict['results'][0]['daily'][days]['wind_scale']
    list = [a, b, c, d, e, f, g]
    return list

def weather_try(city):
    url = 'https://api.seniverse.com/v3/weather/now.json'
    param = {'key': 'ghc8nixp7a89p9qk', 'location': city}
    dict = requests.get(url, params = param).json()
    a = dict['results'][0]['now']['text']
    b = dict['results'][0]['now']['wind_direction']
    c = dict['results'][0]['now']['temperature']
    d = dict['results'][0]['last_update']
    time1 = d[0:10]
    time2 = d[11:16]
    list  = [a, b, c, time1, time2]
    return list

def tp():
    x = input('请输入您要查询的温度单位, c 为摄氏度, f 为华氏度:')
    if x in ['c', 'f']:
        return x
    else:
        print('您的输入有误')
        return tp()

def delay():
    y = input('如果您想立刻查询请输入 now , 如果您想指定时间查询请输入 d : ')
    if y == 'd':
        times = tm()
        return times
    elif y == 'now':
        times = 0
        return times
    else:
        print('您的输入有误')
        return delay()

def tm():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print('现在的时间是', t)
    try:
        h, m = map(int, input('请输入您想开始查询的时间,如13点40分,请输入13 40 >').split())
        if h in range(24) and m in range(60):
            localtime = time.localtime(time.time())
            hours = h - int(localtime.tm_hour)
            mins = m - int(localtime.tm_min)
            secs = 0 - int(localtime.tm_sec)
            t = hours * 3600 + mins * 60 + secs
            return t
        else:
            print('您的输入有误')
            return tm()
    except ValueError:
        print('您的输入有误')
        return tm()

def thk(city, type):
    print('\n多谢等待')
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print('现在的时间是', t)
    weather_list = weather(city, type)
    if type == 'c':
        print(city + '的天气为' + weather_list[0] + ',风向为', end ='')
        print(weather_list[1] + ',温度为' + weather_list[2] + '摄氏度.')
    else:
        print(city + '的天气为' + weather_list[0] + ',风向为', end ='')
        print(weather_list[1] + ',温度为' + weather_list[2] + '华氏度.')
    print('更新时间：', weather_list[3], weather_list[4])
    print('指定时间查询结束请继续输入指令或您要查询的城市名：')

def da():
    try:
        d = int(input('输入数字代表要查询的日期, 输入0代表查询当天实时天气, 输入1-14代表查询未来第几天的天气预报:'))
        if d in range(15):
            return d
        else:
            print('您的输入有误')
            return da()
    except ValueError:
        print('您的输入有误')
        return da()

history_list = []

while True:
    city = input('请输入指令或您要查询的城市名：')
    try:
        none = weather_try(city)
        days = da()
        if days == 0:
            type = tp()
            times_your = delay()
            if times_your > 0:
                Timer(times_your, thk, (city, type)).start()
                weather_list = weather(city, type)
                history_dict = {}
                if type == 'c':
                    k = city + '的天气为' + weather_list[0] + ',风向为' + weather_list[1] + ',温度为' + weather_list[2] + '摄氏度.'
                else:
                    k = city + '的天气为' + weather_list[0] + ',风向为' + weather_list[1] + ',温度为' + weather_list[2] + '华氏度.'
                v = '更新时间:' + weather_list[3] + '/' + weather_list[4]
                history_dict[k] = v
                history_list.append(history_dict)
            else:
                weather_list = weather(city, type)
                if type == 'c':
                    print(city + '的天气为' + weather_list[0] + ',风向为', end ='')
                    print(weather_list[1] + ',温度为' + weather_list[2] + '摄氏度.')
                else:
                    print(city + '的天气为' + weather_list[0] + ',风向为', end ='')
                    print(weather_list[1] + ',温度为' + weather_list[2] + '华氏度.')
                print('更新时间：', weather_list[3], weather_list[4])
                history_dict = {}
                if type == 'c':
                    k = city + '的天气为' + weather_list[0] + ',风向为' + weather_list[1] + ',温度为' + weather_list[2] + '摄氏度.'
                else:
                    k = city + '的天气为' + weather_list[0] + ',风向为' + weather_list[1] + ',温度为' + weather_list[2] + '华氏度.'
                v = '更新时间:' + weather_list[3] + '/' + weather_list[4]
                history_dict[k] = v
                history_list.append(history_dict)
        else:
            type = tp()
            weather_l = weather_future(city, type, days)
            if type == 'c':
                print(city + weather_l[0] + '白天' + weather_l[1] + ',晚上' + weather_l[2], end = '')
                print(',最高' + weather_l[3] + '摄氏度' + ',最低' + weather_l[4] + '摄氏度.')
            else:
                print(city + weather_l[0] + '白天' + weather_l[1] + ',晚上' + weather_l[2], end = '')
                print(',最高' + weather_l[3] + '华氏度' + ',最低' + weathter_l[4] + '华氏度.')
            history_dict = {}
            k = city + weather_l[0]
            if type == 'c':
                v = '白天' + weather_l[1] + ',晚上' + weather_l[2] + ',最高' + weather_l[3] + '摄氏度' + ',最低' + weather_l[4] + '摄氏度.'
            else:
                v = '白天' + weather_l[1] + ',晚上' + weather_l[2] + ',最高' + weather_l[3] + '摄氏度' + ',最低' + weather_l[4] + '华氏度.'
            history_dict[k] = v
            history_list.append(history_dict)

    except KeyError:
        if city == 'help':
            print("输入城市名,按照提示输入指定数字可查询当天实时天气(可切换温度单位或选择当天定时查询)；")
            print("输入城市名,按照提示输入指定数字查询未来14天的天气预报：")
            print("输入 help,查询帮助文档；")
            print("输入 history,获取查询历史；")
            print("输入 quit,退出天气查询系统.")
        elif city == 'history':
            for i in history_list:
                for j in i:
                    print(j, i[j])
        elif city == 'quit':
            exit(0)
        else:
            print('您输入的城市不存在.')
