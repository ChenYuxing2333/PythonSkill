# 斐波那契数 1
fibs = [0,1]
num = int(input('How many Fibonacci numbers do you want? '))
for i in range(num - 2 ):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)
# 初始化数据结构的参数
def init(data):
    data('first') = {}
    data('middle') = {}
    data('last') = {}