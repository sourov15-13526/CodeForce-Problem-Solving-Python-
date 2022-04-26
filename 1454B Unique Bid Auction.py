
"""for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d = []
    for i in list(set(l)):
        if l.count(i)==1:
            d.append(i)
    if len(d)==0:
        print(-1)
    else:
        print(l.index(min(d))+1)"""
        

from collections import Counter
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dictionary = Counter(a)
    b = [k for k, v in dictionary.items() if v == 1]
    if len(b) == 0:
        print(-1)
    else:
        print(a.index(min(b)) + 1)