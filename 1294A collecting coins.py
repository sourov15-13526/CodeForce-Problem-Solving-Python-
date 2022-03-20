for t in range(int(input())):
    a,b,c,n = map(int, input().split())
    s = a+b+c+n
    d = max(a,b,c)*3 - (a+b+c)
    if s%3==0 and n>=d:
        print("YES")
    else:
        print("NO")