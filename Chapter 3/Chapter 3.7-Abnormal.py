try:
    open("abc.txt","r")
    print(name)
except BaseException as msg:
    print("异常了！")
    print(msg)
else:
    print("没有异常！")
finally:
    print("不管异常与否，我都会被执行！")


#raise 抛出异常
from random import randint

#生成一个1到9之间的随机数
num = randint(1,9)

if num % 2 == 0:
    raise NameError("%d is even" %num)
else:
    raise NameError("%d is odd" %num)