n = int(input())
a = sorted(list(map(int, input().split())))
s = 0
k = -1
for i in range(n//2):
    s+=(a[i]+a[k])**2
    k-=1
print(s)
    