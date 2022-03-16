i=lambda:map(int,input().split());n,k=i();l=list(i());
print(sum(v>=max(1,l[k-1])for v in l))


i=lambda:map(int,input().split())
n,k=i()
l=list(i())
print(sum(v>=max(1,l[k-1])for v in l))


f=lambda:map(int,input().split())
n,k=f()
s=list(f())
print(sum(x>=max(1,s[k-1]) for x in s))

i = lambda: map(int, input().split());
n, k = i();
l = list(i());

print(sum(i >= max(1, l[k - 1]) for i in l))




n,k=map(int,input().split())
a=list(map(int,input().split()))
print(sum(v>=max(1,a[k-1])for v in a))



d=int
e=input
k=d(e().split()[1])
s=list(map(d,e().split()))
print(sum([i>0 for i in s if i >= s[k-1]]))