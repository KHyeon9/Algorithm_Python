mo = ['a', 'e', 'i', 'o', 'u']

while 1:
    s = input()

    if s == '#':
        break

    if s[0] in mo:
        print(s + 'ay')
        continue
    for i in range(len(s)):
        if s[i] in mo:
            print(s[i:] + s[:i] + 'ay')
            break
    else:
        print(s + 'ay')
