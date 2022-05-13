while 1:
    try:
        s, t = input().split()
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
                if len(s) == j:
                    print("Yes")
                    break
        else:
            print("No")
    except:
        break