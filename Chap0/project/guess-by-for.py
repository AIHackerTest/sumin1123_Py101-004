
# coding: utf-8

# In[4]:


from sys import exit

import random
answer = random.randint(0,20)

def close():
    exit(0)

for n in range(1,11):
    x = input("请输入0~20之间的任意数字>")
    if x.isdigit():
        guess = int (x)
        if guess == answer:
            print("答对了，你用了%d次，游戏结束" %n)
            close()
        elif guess > answer:
            if n != 10:
                print("大了，请重新输入，你还有%s机会"% (10-n))
            else:
                print("没有答对，次数用完了")
        else:
            if n != 10:
                print("小了，请重新输入，你还有%s次机会" % (10-n))
            else:
                print("没有答对，次数用完了")
    else:
        print("请确保你输入的是数字，你还有%s机会" % (10-n))

