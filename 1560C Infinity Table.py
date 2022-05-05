import math
for i in range(int(input())):
    k=int(input())
    t=int(k**0.5)
    p=k-t**2
    if(p>0):
        if(p<=t):
            print(p,t+1)
        else:
            print(t+1,(t+1)**2-k+1)
    else:
        print(t,1)
  