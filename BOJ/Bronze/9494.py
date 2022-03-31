while 1:
    n = int(input())
    result = 0
    if n == 0:
        break
    for _ in range(n):
        s = input()
        if result > len(s):
            continue
        for word in s[result:]:
            if word == ' ':
                break
            result += 1
    print(result + 1)


