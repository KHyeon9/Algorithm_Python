m = "aiyeou"
j = "bkxznhdcwgpvjqtsrlmf"
while 1:
    try:
        s = input()
        result = ""
        for i in s:
            c = i.lower()
            if c in m:
                num = (m.index(c) + 3) % len(m)
                if i.isupper():
                    result += m[num].upper()
                else:
                    result += m[num]
            elif c in j:
                num = (j.index(c) + 10) % len(j)
                if i.isupper():
                    result += j[num].upper()
                else:
                    result += j[num]
            else:
                result += c
        print(result)
    except EOFError:
        break