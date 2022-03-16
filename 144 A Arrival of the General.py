t = int(input())
s = list(map(int, input().split()))
a = s.index(max(s))
s.pop(a)
b = s[::-1].index(min(s))
print(a+b)


