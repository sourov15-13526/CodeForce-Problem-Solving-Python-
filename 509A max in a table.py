n = int(input())
t = [1]*n
for r in range(1,n):
    for i in range(1,n):
        t[i] = t[i]+t[i-1]
print(t[n-1])


