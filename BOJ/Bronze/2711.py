for _ in range(int(input())):
    n, s = input().split()
    r = ''
    for i in range(len(s)):
        if i == int(n) - 1:
            continue
        r += s[i]
    print(r)