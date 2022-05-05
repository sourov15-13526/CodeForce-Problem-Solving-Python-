
# not done
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = [0]
    while len(a)!=0:
        minimum = min(a[0],a[-1])
        maximum = max(a[0],a[-1])
        if minimum >= c[-1]:
            c.append(minimum)
            if a[0]<=a[-1]:
                a.pop(0)
            else:
                a.pop()
        elif maximum >= c[-1]:
            c.append(maximum)
            if a[0]<=a[-1]:
                a.pop()
            else:
                a.pop(0)
        else:
            break
    print(n-len(c)+1)
    
    