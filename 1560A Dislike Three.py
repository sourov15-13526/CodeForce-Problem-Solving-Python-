L = [i for i in range(1667) if i%3 != 0 and str(i)[-1] != '3']
n = int(input())
for a in range(n):
    print(L[int(input())-1])
