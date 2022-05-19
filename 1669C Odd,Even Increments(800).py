for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    od = []
    ev = []
    for i in range(n):
        if i%2==0:
            ev.append(a[i])
        else:
            od.append(a[i])
    f1 = 0
    f2 = 0
    if od[0]%2==0:
        for x in od:
            if x%2!=0:
                f1+=1
    elif od[0]%2!=0:
        for x in od:
            if x%2==0:
                f1+=1           
    
    if ev[0]%2==0:
        for y in ev:
            if y%2!=0:
                f2+=1
    elif ev[0]%2!=0:
        for y in ev:
            if y%2==0:
                f2+=1
                
    if f1==0 and f2==0:
        print('YES')
    else:
        print('NO')
    