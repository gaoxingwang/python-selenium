#导入time模块
'''
import time
print(time.ctime())
'''

#导入time模块下ctime()方法
'''
from time import ctime
print(ctime())
'''

#导入time模块下所有方法
from time import *
print(ctime())
print("sleep 2 sec ...")
sleep(2)
print(ctime())