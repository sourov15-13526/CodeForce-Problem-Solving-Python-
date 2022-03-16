n = input()
u = 0
l = 0
for i in n:
    if i.isupper():
        u = u+1
    else:
        l = l+1
print(n.upper() if u>l else n.lower())

