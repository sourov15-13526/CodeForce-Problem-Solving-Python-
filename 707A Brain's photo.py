from ast import Str
n,m = map(int, input().split())
flag = 0
for t in range(n):
    l = list(input().split())
    if "C" in l or "M" in l or "Y" in l:
        flag+=1
if flag==0:
    print("#Black&White")
else:
    print("#Color")
    
    