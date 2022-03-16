for i in range(5):
    a = input().split()
    if "1" in a:
        res = abs(i-2) + abs(a.index("1")-2)
print(res)


