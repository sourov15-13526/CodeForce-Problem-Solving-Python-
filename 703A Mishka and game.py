mishka = 0
chris = 0
for t in range(int(input())):
    m,c = map(int,input().split())
    if m>c:
        mishka+=1
    elif c>m:
        chris+=1
    else:
        mishka = mishka
        chris = chris
if mishka>chris:
    print("Mishka")
elif(chris>mishka):
    print("Chris")
else:
    print("Friendship is magic!^^")
    