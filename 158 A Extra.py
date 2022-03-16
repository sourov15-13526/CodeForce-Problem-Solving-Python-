n,k=map(int,input().split())
a=list(map(int,input().split()))
print(sum([i>0 for i in a if i >= a[k-1]]))
