for t in range(int(input())):
    n = int(input())
    st = input()
    
    flag = 1
    for i in range(n-1):
        if st[i] != st[i+1]:
            if st[i] in st[i+1:]:
                flag = 0
                break
    if flag == 1:
        print("YES")
    else:
        print("NO")