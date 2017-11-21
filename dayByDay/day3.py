'''
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''

import math

# x = 'se'
const1 = 100
const2 = 168
# for x in range(1,85):
#     if (math.sqrt(x+const1).is_integer()) and (math.sqrt(x + const1 + const2).is_integer()):
#         print('这个整数是：%d'% x)

x = 100.09
y = 100.0
print(x.is_integer()) #返回False
print(y.is_integer()) #返回True
