from math import ceil


for t in range(int(input())):
    n,k = map(int, input().split())
    if n>k:
        if n%k == 0:
            print(1)
        else:
            print(2)
    else:
        print(ceil(k/n))