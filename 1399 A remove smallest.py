t = int(input())
for k in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    A = "YES"
    for i in range(n-1):
        if (a[i] < a[i+1]-1):
            print("NO")
            break
    else:
        print(A)







