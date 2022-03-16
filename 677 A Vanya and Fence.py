n,m = map(int, input().split())
t = map(int, input().split())
sum = 0
for i in t:
    if i>m:
        sum+=2
    else:
        sum+=1
print(sum)
