row = 1
while row <= 9:
    col =1
    while col <=row:
        print("%d * %d = %d" %(col,row,row * col),end="\t")
        col = col + 1
    print("")
    row = row + 1
# 九九乘法表