print(sum(1 if '+' in input() else -1 for i in range(int(input())) ))


x=0
for i in range(int(input())):
  x+=input()[1]=='+' or -1
print(x)


X = 0
for _ in range(int(input())):
    X += 1 if '++' in input() else -1
print(X)


l = ''.join((input() for x in range(int(input()))))
print(l.count('++') - l.count('--'))


q = int(input())
c = 0
for _ in q*' ':
  c += (input()[1] == '+' and 1 or -1)
print(c)


n = int(input())
x = 0
for i in range(n):
	if '+' in input():
		x += 1
	else:
		x -= 1
print(x)



n = int(input())
k=0
for i in range(n):
	j = input()
	if '++' in j:
		k=k+1
	else:
		k=k-1
print(k)


n = int(input())
x = 0
for a in range(n):
	op = input()
	x = x+1 if op[1]=="+" else x-1
print (x)