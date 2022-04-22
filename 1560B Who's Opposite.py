for t in range(int(input())):
    a,b,c=map(int,input().split())
    d=abs(a-b)
    if d<min(a,b) or c>2*d:
        print(-1)
    else:
        print(c+d if c<=d else c-d)
    
  
    
    