for t in range(int(input())):
    a,b,n=map(int,input().split())
    c = 1
    while(a%2==0):
        a/=2
        c*=2
    while(b%2==0):
        b/=2
        c*=2
    if c>=n:
        print("YES")
    else:
        print("NO")