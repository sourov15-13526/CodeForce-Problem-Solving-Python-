for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = 0
    for j in range(n):
        m += max(a[j]-min(a),b[j]-min(b))
    print(m)