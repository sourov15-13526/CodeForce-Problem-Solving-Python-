n = int(input())
m = map(int, input().split())
sum = 0
for i in m:
    sum = sum+i
print(sum/n)


#print(1/int(input())*sum(map(int,input().split())))