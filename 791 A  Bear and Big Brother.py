a,b = map(int, input().split())
L = 0
B = 0
count = 0
while True:
    if (L>B):
        break
    else:
        L = a*3
        B = b*2
        a = L
        b = B
        count+=1
print(count)
