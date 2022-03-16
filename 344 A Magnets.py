n = int(input())
a = input()
c = 0
for i in range(n-1):
    b = input()
    if a!=b:
        c = c+1
    a = b

print(c+1)


# a = [input() for i in range(n)]; x = 1