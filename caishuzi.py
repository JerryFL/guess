import random
start = input('请决定随机数字的范围的开始值')
end = input('请决定随机数字范围的结束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count = count + 1
    num=input('请输入随机数字：')
    num=int(num)
    if num == r:
        print('你猜中了')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('这是你猜的第', count,'次')

