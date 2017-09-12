#! python3
# coding = utf-8

import requests
import json
from datetime import datetime

url = 'https://api.seniverse.com/v3/weather/now.json' # 心知天气API调用 网址
dict = {}

while True:
    x = input('请输入需要查询天气的城市名称，中文、英文均可：>') # 输入城市名称
    p = {'key' : 'ghc8nixp7a89p9qk','location' : x,'language' : 'zh-Hans','unit' : 'c'} # 把requests.get(url,params{})格式里的params字典提前设置好

    try:
        result = requests.get( url , params = p , timeout=60 ) # result已获得API返回的数据
        r = json.loads(result.text) # result.text把result转为文本，再通过json.loads转化为字典
        weather = r['results'][0]['now']['text'] # weather是天气
        temp = r['results'][0]['now']['temperature'] # temp定义为温度
        nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(x+'的天气是：'+weather+'，气温是：'+ temp+ '摄氏度；')
        print('查询时间是：'+nowtime)
        k = x+'的天气是：'+weather+'，气温是：'+ temp+ '摄氏度；'
        v = '查询时间是：'+nowtime
        dict[k] = v

    except:
        if x in 'h,help':
            print('''
            输入查询天气的城市；
            输入h或help查看帮助；
            输入quit退出程序；
            输入history查看历史；
            ''')
        elif x in 'quit':
            break
        elif x in 'history':
            for k in dict.keys():
                print(k,dict[k])
        else:
            print('请输入正确的命令')
