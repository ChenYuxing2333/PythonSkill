# If 语句
num = int(input('Enter a number: '))
if num > 0:
    print('The number is positive')
elif num < 0:
    print('The number is negative')
else:
    print('The number is zero')
# while 循环
x = 1
while x <= 100:
    print(x)
    x += 1
# for 循环
numbers = [0,1,2,3,4,5,6,7,8,9]
for numbers in numbers:
    print(numbers)
# fot 循环 2
for number in range(1,101):
    print(number)
# 循环中的 else 子句
from math import sqrt
for n in range(99,81,-1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
    else:
        print("Didn't find it!")



