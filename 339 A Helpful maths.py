print("+".join(sorted(input().split('+'))))


l=input().split('+')
l.sort()
print('+'.join(l))


s=input()
print('+'.join(sorted(s.replace('+',''))))