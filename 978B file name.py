
t = int(input())
n = input()
c = 0
for i in range(t-2):
    if n[i:i+3]=='xxx':
        c+=1
print(c)