t = int(input())
n = [int(input()) for i in range(t)]
for a in n:
    if (a/2)%2==0 and (a/2)>1:
        print("YES")
        l = []
        for i in range(2,a+1,2):
            l.append(i)
        for i in range(1,a-1,2):
            l.append(i)
        l.append((a-1)+(a//2))
        print(*l)

    else:
        print("NO")


"""t = int(input())
for _ in range(t):
    n = int(input())
    if (n / 2) % 2 == 0:
        print('YES')
        print(' '.join([str(i) for i in range(2, n + 1, 2)] + [str(i) for i in range(1, n - 1, 2)] + [str((n - 1) + n // 2)]))
    else:
        print('NO')






t = int(input())

for _ in range(0, t):
    m = int(input())
    if m % 4 != 0:
        print("NO")
    else:
        print("YES")
        a = []
        for i in range(1, int(m / 2 + 1)):
            a.append(2 * i)
        for i in range(1, int(m / 4 + 1)):
            a.append(2 * i - 1)
        for i in range(int(m / 4 + 1), int(m / 2 + 1)):
            a.append(2 * i + 1)
        print(*a)"""