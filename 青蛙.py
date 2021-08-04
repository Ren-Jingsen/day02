sum = 0 #一共爬了多少
i = 3 #白天爬的距离
k = 2 #晚上掉 距离
day = 0 #爬的天数
while sum <= 20:
    if sum + i < 20:
       sum = sum - k
       day = day + 1
    sum = sum + i
print('青蛙爬',day,'天可以爬出去')