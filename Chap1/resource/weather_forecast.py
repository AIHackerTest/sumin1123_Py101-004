# -*- coding:utf-8 -*- 

# 读取原文明，生成“城市名”：“天气”的字典
f = open('weather_info.txt', 'r', encoding='UTF-8')
dict = {}
for line in f:
    line = line.strip().split(',')
    dict[line[0]] = line[1]

# 定义his为保存历史的字典
his = {}

while True:
    x = input("请输入查询城市>")

    if x in dict: # 如果输入包含在字典的key里
        print(x,dict[x]) # 输出天气
        his[x]= dict[x]  # 存入历史字典

    elif x in ('help','h'):
        print(
        '''
        这是一个天气查询程序；
        输入help或h，查看帮助；
        输入history，查看查询历史；
        输入quit，退出程序；
        ''')
		
    elif x == 'quit':
        print('程序马上退出')
        exit(0)
    
    elif x == 'history':
        print("您的历史查询是:")
        for i in his:
            print(i, his[i])

    else:
        print('您输入的城市暂不提供查询')