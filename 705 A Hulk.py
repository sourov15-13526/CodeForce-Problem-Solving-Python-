n = int(input())
s = ""
for i in range(1,n+1):
    if i%2 != 0:
        s+="I hate"
    else:
        s += "I love"
    if i<n:
        s+=" that "
    if i==n:
        s+=" it"

print(s)


