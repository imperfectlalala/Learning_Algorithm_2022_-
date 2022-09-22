#清屏
import os
os.system("cls")
#创建备用列表
num_list = []
#读取输入数值，并传入列表中去
a,b,c,d = map(int,input("输入四个数字，注意要用空格隔开:").split())
num_list.append(a)
num_list.append(b)
num_list.append(c)
num_list.append(d)
#找出列表中最大的数字
max_numbers = max(num_list)
print("数列中最大值为：{}".format(max_numbers))