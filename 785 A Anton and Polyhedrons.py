t = int(input())
sum = 0
for i in range(t):
    n = input()
    if (n == "Icosahedron"):
        sum = sum+20
    elif (n == "Cube"):
        sum = sum+6
    elif(n == "Tetrahedron"):
        sum = sum+4
    elif(n == "Octahedron"):
        sum = sum+8
    elif (n == "Dodecahedron"):
        sum = sum+12

print(sum)