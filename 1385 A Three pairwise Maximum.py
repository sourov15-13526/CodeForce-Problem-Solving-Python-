for i in range(int(input())):
    x,y,z = sorted(map(int,input().split()))
    if y==z:
        print("YES")
        print(x,x,y)
    else:
        print("NO")