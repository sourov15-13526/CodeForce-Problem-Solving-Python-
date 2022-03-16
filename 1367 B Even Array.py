for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    even = 0
    odd = 0
    for i in range(n):
        if i%2 != l[i]%2:
            if i%2 == 0:
                even+=1
            else:
                odd+=1
    print([-1,even][even==odd])



