t = int(input())
c = 0; d = 0
for i in range(t):
    n = int(input())
    a = map(int, input().split())
    for s in a:
        if s%2 != 0:
            c+=1
        else:
            d+=1
    if (c == n and c%2 != 0):
        print("YES")
    elif (c >= 1 and c != n):
        print("YES")
    else:
        print("NO")
    c = 0;d = 0


