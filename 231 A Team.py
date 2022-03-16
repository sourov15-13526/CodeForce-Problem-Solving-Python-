n = int(input())
s = 0
for i in range(n):
    z = input()
    c = z.count('1')
    if c>=2:
        s = s+1
print(s)

#print(sum(input().count('1')>1for x in [0]*int(input())))

