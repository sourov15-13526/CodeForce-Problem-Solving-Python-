k,n,w = map(int, (input()).split())
sum = 0
for a in range(1,w+1):
    sum += k*a
if (n>=sum):
    print('0')
else:
    print(sum - n)
