for t in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    if l.count(1)==0 and l.count(2)%2==0:
        print("YES")
    elif l.count(2)==0 and l.count(1)%2==0:
        print("YES")
    elif l.count(1)%2==0 and l.count(1)!=0:
        print("YES")
    else:
        print("NO")