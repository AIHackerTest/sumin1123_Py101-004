#! python3
# coding: utf-8

import random
from sys import exit

num = random.randint(1,20)
guess = 0
time = 0
print("这是一个猜数字的小游戏，系统会自动生成一个20以内的数字", end = '')
print("(包括20)，您一共有10次机会：")

def right(shu):
    print("恭喜您答对了 答案就是 %d \n游戏结束" % shu)
    exit(0)

def over():
    print("机会用完了\n游戏结束")
    exit(0)

while True:
    guess_num =input("请输入数字：")
    if guess_num.isdigit():
        guess = int(guess_num)
        if guess < num:
            print("小了")
        elif guess > num:
            print("大了")
        else:
            right(num)
        time = time + 1
        if time == 10:
            over()
        else:
            print("你还有", 10 - time, "次机会可以输入")
    else:
        print("请确保您输入的是数字")
