a = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}


while 1:
    s = list(input())
    r = 0

    if s[0] == '#':
        break

    else:
        for i in range(len(s)):
            r += a[s[i]] * (8 ** (len(s) - 1 - i))

    print(r)