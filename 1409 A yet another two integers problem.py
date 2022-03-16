import math
for i in range(int(input())):
    x,y = map(int, input().split())
    d = abs(x-y)
    res = d/10
    print(math.ceil(res))