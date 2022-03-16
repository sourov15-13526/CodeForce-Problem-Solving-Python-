t = int(input())
l = list(map(int, input().split()))
a = 0
b = 0
for i in range(t):
    a+=l[i]
    if l[i]==-1 and a<0:
        a = 0
        b+=1
print(b)
