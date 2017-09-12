import requests
from datetime import datetime

dict = {} # 定义dict为存放历史查询字典

def getip(x): # 用户输入城市后，获取城市ip
    baidumapurl = 'http://api.map.baidu.com/geocoder/v2/' # 百度地图QPI调用地址
    baidup = {'address' : x , 'output' : 'json' , 'ak' : '2OXG7ZbGSzXailco5nG0hLxQbzL5fdHn'} # request.get的参数，百度的key叫ak
    baiduresult = requests.get(baidumapurl,params=baidup).json()
    lan = baiduresult['result']['location']['lat']
    lng = baiduresult['result']['location']['lng']
    ip.append(lan)
    ip.append(lng)
    # print(baiduresult)
    print(x+'的城市坐标，经度：', ip[0] , '纬度：',ip[1] )
    return ip # 将查询出来的城市ip返回成一个列表

while True:
    ip = []
    x = input('请输入城市名称：>')
    try:
        getip(x) # 去获取城市ip的函数
        api = 'abddc3d0e6a5b9500d9b97e31df5611b' # Dark Sky API的key
        lat = ip[0]
        lng = ip[1]
        # print(lat,lng)
        url = "https://api.darksky.net/forecast/%s/%s,%s" % (api, lat, lng) # 因API的格式https://api.darksky.net/forecast/[key]/[latitude],[longitude]，所以使用了格式化字符串
        param = {'lang' : 'zh' , 'units' : 'si' ,'exclude' : 'currently'}
        r = requests.get(url,params=param).json()
        weather = r['hourly']['summary']
        temp = r['hourly']['data'][0]['temperature']
        nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 获取当前时间
        print(weather,temp,nowtime)

        print(x , '的天气是：' , weather , '气温是：' , temp , '摄氏度。' , '查询时间：' , nowtime)

        k = x+'的天气是：'+weather+'气温是：%s' % temp+'摄氏度。' # temp 前面使用了格式化字符，没有用+，因temp是数值
        v = '查询时间：'+nowtime
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
