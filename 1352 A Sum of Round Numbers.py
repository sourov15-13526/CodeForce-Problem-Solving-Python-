for i in range(int(input())):
    n = input()
    l = len(n)
    L = []
    for k in n:
        if k != '0':
            L.append(k+'0'*(l-1))
        l-=1
    print(len(L))
    print(*L)



