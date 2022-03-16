t = int(input())
c = list(map(int, input().split()))
m = max(c)
sum = 0
for i in range(t):
    sum+=(m-c[i])
print(sum)

