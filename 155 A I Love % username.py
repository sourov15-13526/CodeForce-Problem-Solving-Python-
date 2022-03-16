t = int(input())
n = list(map(int, input().split()))
count = 0
for i in range(1,t):
    if n[i]>max(n[:i]) or n[i]<min(n[:i]):
        count+=1
print(count)


