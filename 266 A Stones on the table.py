n = int(input())
s = str(input())
count = 0
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        count += 1
print(count)



"""input()
s = input()
print(sum([s[i]==s[i-1] for i in range(1, len(s))]))"""