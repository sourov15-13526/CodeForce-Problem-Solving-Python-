for t in range(int(input())):
    a,b = map(int, input().split())
    d = b-a
    if (d>0 and d%2==0) or (d<0 and abs(d)%2!=0):
        print(2)
    elif (d>0 and d%2!=0) or (d<0 and abs(d)%2==0):
        print(1)
    else:
        print(0)
    