k2,k3,k5,k6 = map(int, input().split())
b = min(k2,k5,k6)
s = min((k2-b),k3)

res = (b*256)+(s*32)
print(res)