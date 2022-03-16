n = int(input())
for i in range(1,n+1):
    if i>3:
        c = 0
        for k in range(1,i+1):
            if i%k == 0:
                c+=1
        if c>2:
            con = 0
            for j in range(1, (n - i + 1)):
                if (n - i) % j == 0:
                    con += 1
            if con > 2:
                print(i, n - i)
                break

