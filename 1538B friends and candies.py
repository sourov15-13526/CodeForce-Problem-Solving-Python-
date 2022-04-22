for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    if sum(a)%len(a)==0:
        k = sum(a)/len(a)
        for i in a:
            if i>k:
                ans+=1
        print(ans)
    else:
        print(-1)