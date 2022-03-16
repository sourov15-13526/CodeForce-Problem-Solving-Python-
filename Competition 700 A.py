for i in range(int(input())):
    s = input()
    l = len(s)
    full = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    nes = ''
    for k in range(l):
        if s[k] in full and k%2==0:
            full.remove(s[k])
            nes+=min(full)
            full.append(s[k])
        else:
            full.remove(s[k])
            nes+=max(full)
            full.append(s[k])
    print(nes)
