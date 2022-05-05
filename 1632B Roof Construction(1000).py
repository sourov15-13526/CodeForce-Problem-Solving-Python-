for t in range(int(input())):
    n=int(input())
    d=[]
    s=0
    while 2**s<n:
        s+=1
    s=s-1
 
    for k in range(1,n):
        if 2**s==k:
            d.append(0)
            d.append(2**s)
        else:
            d.append(k)
    print(*d) 