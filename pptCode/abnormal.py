'''
try:
	open("abc.txt",'r')
except FileNotFoundError:
	print("异常了")
'''
'''
try:
	print(aa)
except FileNotFoundError:
	print("异常了")
'''
'''
try:
	print(aa)
except NameError:
	print("这是一个name异常")
'''
'''
try:
	open("abc.txt",'r')
	print(aa)
except Exception:
	print("异常了")
'''
'''
try:
	open("abc.txt",'r')
	print(aa)
except BaseException:
	print("异常了")
'''
'''
try:
	open("abc.txt",'r')
	print(aa)
except BaseException as msg:
	print(msg)
'''
'''
try:
	aa = "异常测试"
	print(aa)
except BaseException as msg:
	print(msg)
else:
	print("没有异常啊")
'''
'''
try:
	print(aa)
except BaseException as msg:
	print(msg)
finally:
	print("有没有异常我都会执行")
'''
'''
try:
	aa = "异常测试"
	print(aa)
except BaseException as msg:
	print(msg)
finally:
	print("有没有异常我都会执行")
'''

from random import randint

number = randint(1,9)

if number % 2 == 0:
	raise NameError("%d is a even" % number)
else:
	raise NameError("%d is a odd" % number)


























