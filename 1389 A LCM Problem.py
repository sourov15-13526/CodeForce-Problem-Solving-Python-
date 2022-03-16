for i in range(int(input())):
    l,r = map(int,input().split())
    d = r-l
    if d>=2:
        for j in range(r,0,-1):
            for k in range(1,r):
                for m in range(1,j*l+1):
                    if m%k==0 and m%j==0 and m<=r:
                        print(k,j)
                        break
    else:
        print("-1 -1")
"""for i in range(10,0,-1):
    print(i)"""