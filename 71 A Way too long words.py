n = int(input())
for i in range(n):
    string = str(input())
    l = len(string)
    if (l > 10):
        print(string[0:1]+str(l-2)+string[l-1:l])
    else:
        print(string)

"""for j in[0]*int(input()):a=input();s=len(a)-2;print([a,a[0]+str(s)+a[-1]][s>8])"""



