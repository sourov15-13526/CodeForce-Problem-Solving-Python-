a,b = map(int, input().split())
s = str(input())
for i in range(b):
    s = s.replace("BG","GB")

print(s)
