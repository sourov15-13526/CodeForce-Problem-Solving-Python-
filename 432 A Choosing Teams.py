n,k = map(int, input().split())
y = list(map(int, input().split()))
t = 0
for i in range(n):
    if (5-y[i])>=k:
        t+=1
print(t//3)
