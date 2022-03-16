n = int(input())
p = input().split()
q = input().split()

print("I become the guy." if len(set(p[1:]+q[1:]))==n else "Oh, my keyboard!")