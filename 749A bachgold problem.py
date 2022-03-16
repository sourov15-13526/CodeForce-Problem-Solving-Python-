n = int(input())
l = [2]
if n%2==0:
    l=l*(n//2)
else:
    l=l*((n-3)//2)
    l.append(3)
print(len(l))
print(*l)