from os import sep


for t in range(int(input())):
    a = input()
    b = sorted(a)
    if b[0]==b[-1]:
        print(-1)
    else:
        print(*b, sep="")