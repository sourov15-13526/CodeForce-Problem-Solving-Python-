from math import ceil


for t in range(int(input())):
    m,n = map(int, input().split())
    print(ceil((m*n)/2))