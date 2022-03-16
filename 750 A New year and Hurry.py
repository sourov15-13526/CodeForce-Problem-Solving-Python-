n,k = map(int, input().split())
x = 240-k
sum = 0
cont = 0
for i in range(1,n+1):
    sum += 5*i
    if sum<=x:
        cont += 1
    else:
        break
print(cont)



