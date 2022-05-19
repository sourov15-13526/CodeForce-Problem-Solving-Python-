for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    sr = sorted([[a[i],i] for i in range(n)], reverse= True)
    res = [0]
    p = 1
    m = -1
    for i in range(n):
        if i%2==0:
            res.append(p)
            p+=1
        else:
            res.append(m)
            m-=1
            
    sum = 0
    for k in range(n):
        x = 2*abs(res[0]-res[k+1])*sr[k][0]
        sum+=x 
    print(sum)
    print(*res)