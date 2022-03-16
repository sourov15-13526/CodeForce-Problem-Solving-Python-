n = input()
l = []
for i in n:
    if i.isalpha():
        l.append(i)
print(len(set(l)))