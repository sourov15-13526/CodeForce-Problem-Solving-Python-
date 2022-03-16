L = list(map(int, input().split()))
m = max(L)
for i in range(len(L)-1):
    p = m - min(L)
    L.remove(min(L))
    print(p,end=" ")