for i in range(int(input())):
    x,y,n = map(int, input().split())
    p = (n-y)//x
    k = (p*x)+y
    print(k)
