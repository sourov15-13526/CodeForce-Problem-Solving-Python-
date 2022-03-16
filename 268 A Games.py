n = int(input())
L = []; K = []; sum = 0
for i in range(n):
    a,b = map(int, input().split())
    L.append(a); K.append(b)
for i in L:
    sum += K.count(i)

print(sum)
