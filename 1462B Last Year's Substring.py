for t in range(int(input())):
    n = int(input())
    s = input()
    lst = [s[:4],s[:3]+s[-1],s[:2]+s[-2:],s[0]+s[-3:],s[-4:]]
    if '2020' in lst:
        print('YES')
    else:
        print('NO') 