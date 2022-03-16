a,b = map(int, input().split())
L = []
if a>b:
    L.append(b)
    L.append((a-b)//2)
elif a==b:
    L.append(a)
    L.append('0')
else:
    L.append(a)
    L.append((b-a)//2)
print(*L)