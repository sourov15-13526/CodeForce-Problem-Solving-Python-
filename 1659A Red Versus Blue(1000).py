for t in range(int(input())):
    n,r,b = map(int, input().split())
    b+=1
    x = r//b
    y = r%b
    ans = ""
    
    for i in range(y):
        ans+=(x+1)*"R"+"B"
    for j in range(b-y):
        ans+=x*"R"+"B"
    ans = ans[:-1]
    print(ans)