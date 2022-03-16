for i in range(int(input())):
    x,y = map(int, input().split())
    a = 0
    b = 0
    st = input()
    for j in st:
        if j=="U" and b<y:
            b+=1
        elif j=="D" and b>y:
            b-=1
        elif j=="R" and a<x:
            a+=1
        elif j=="L" and a>x:
            a-=1
    if a==x and b==y:
        print("YES")
    else:
        print("NO")



