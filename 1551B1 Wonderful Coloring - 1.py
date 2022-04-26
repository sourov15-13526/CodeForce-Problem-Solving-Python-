from cgi import print_arguments


for t in range(int(input())):
    s = input()
    ans = 0
    for i in list(set(s)):
        if s.count(i)>1:
            ans+=1
        ans+=1
    print(ans//2)