# '''
# 题目：
# 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
# '''
#
# def getBonus(profit):
#     # try:
#     #     if type(profit) != int:
#     #         print("pls enter a number")
#     # except TypeError as e:
#     #     print(e)
#
#         bonus = 0.0
#         limit = [0,100000, 200000, 400000, 600000, 1000000]
#         rate = [0.1, 0.075 ,0.05, 0.03, 0.015,0.01]
#         # limit = [1000000,600000, 400000, 200000,100000,0]
#         # rate = [0.01,0.015,0.03,0.05, 0.075 ,0.1 ]
#
#         # for idx in [5,4,3,2,1,0]:
#         for idx in range(0,6):
#             if profit>limit[idx]:
#                 bonus += (profit-limit[idx]) * rate[idx]
#                 # print(bonus)
#                 profit = limit[idx]
#
#         return bonus
#
# if __name__=='__main__':
#     print(getBonus(120000))
#
#

#使用list的方式实现
# i = int(input('净利润:'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print ('fd',(i-arr[idx])*rat[idx])
#         i=arr[idx]
# print (r)


#使用dict的方式实现
i = int(input('净利润:'))
bonusRate = {1000000:0.01,600000:0.015,400000:0.03,200000:0.05,100000:0.075,0:0.1}

keys = bonusRate.keys()
# keys.sort()
# keys.reverse()

r=0

for key in keys:
    if i > key:
        r += (i-key) * bonusRate.get(key)
        i = key

print("今年的奖金为：", r,"元。")