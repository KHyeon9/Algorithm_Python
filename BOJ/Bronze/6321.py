for j in range(int(input())):
    s = input()
    r = ''
    for i in s:
        o = ord(i) + 1
        if o == 91:
            r += 'A'
        else:
            r += chr(o)
    print(f"String #{j + 1}")
    print(r)
    print()
