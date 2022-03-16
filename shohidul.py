L = []
L2 = []
for i in range(int(input())):
    a= input()
    L.append(a)
    L2.append(len(a))
m = max(L2)
for i in range(0,len(L)):
    for k in range(m-len(L[i])):
        print(" ",end="",)
    print(L[i])

