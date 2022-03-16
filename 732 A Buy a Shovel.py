k,r = map(int, input().split())
cont = 1
while ((cont*k)-r)%10 != 0 and (cont*k)%10!= 0:
    cont+=1
print(cont)


