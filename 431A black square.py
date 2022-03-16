a1,a2,a3,a4 = map(int, input().split())
str = input()
cal = 0
for i in range(len(str)):
    if str[i]=='1':
        cal+=a1
    elif(str[i]=='2'):
        cal+=a2
    elif(str[i]=='3'):
        cal+=a3
    else:
        cal+=a4
print(cal)
    