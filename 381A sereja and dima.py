n = int(input())
l = list(map(int, input().split()))
s = True
d = False
sp = 0
dp = 0
for i in range(n):
    if s:
        if l[0]>l[-1]:
            sp+=l[0]
            l.remove(l[0])
        else:
            sp+=l[-1]
            l.remove(l[-1])
        s = False
        d = True
    else:
        if l[0]>l[-1]:
            dp+=l[0]
            l.remove(l[0])
        else:
            dp+=l[-1]
            l.remove(l[-1])
        s = True
        d = False
print(sp,dp)
        

