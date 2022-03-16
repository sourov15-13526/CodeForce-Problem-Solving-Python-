for i in range(int(input())):
    a,b = map(int, input().split())
    print(max(min(a,b)*2,a,b)**2)
    