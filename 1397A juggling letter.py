t=int(input())
for i in range(t):
    s=''
    n=int(input())
    for j in range(n):
        str=input()
        s=s+str
    l=[]
    flag=1
    for a in s:
      l.append(s.count(a))
    L = list(set(l))
    for i in L:
        if(i%n!=0):
         flag=0
         break
    if(flag==0):
       print('NO')
    else:
       print('YES')