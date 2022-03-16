n = int(input())
L = list(map(int, input().split()))
a = L.count(1)
b = L.count(2)
c = L.count(3)

if a==0 or b ==0 or c == 0:
    print('0')
else:
    print(min(a,b,c))
    for i in range(min(a,b,c)):
        print(L.index(1)+1,L.index(2)+1,L.index(3)+1)
        L[L.index(1)],L[L.index(2)],L[L.index(3)] = 0,0,0