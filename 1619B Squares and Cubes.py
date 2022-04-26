from ctypes import Union


for t in range(int(input())):
    n = int(input())
    x = 1
    y = 1
    l1 = []
    l2 = []
    while True:
        if x**2>n:
            break
        l1.append(x**2)
        x+=1
        
    while True:
        if y**3>n:
            break
        l2.append(y**3)
        y+=1
    
    res = set(l1).union(set(l2))
    print(len(res))