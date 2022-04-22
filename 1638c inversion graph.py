from sys import maxsize


for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    p_i=0
    max=l[0]
    component=1
    for i in range(1,n):
        if(l[i]>max):
            if(l[p_i]<=i):
                component+=1
            p_i=i
            max=l[i]
    print(component)
    
    