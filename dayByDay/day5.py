'''
输入三个整数x,y,z，请把这三个数由小到大输出。
'''
def sort_num():
    count = int(input('输入个数：'))
    num_list = []
    if count > 0:
        for i in range(count):
            num = int(input('输入整数数字：'))
            num_list.append(num)
            num_list.sort(reverse=True)
        print(num_list)
    else:
        print('请检查输入的个数')

if __name__=='__main__':
    try:
        sort_num()
    except Exception as e:
        print(e)