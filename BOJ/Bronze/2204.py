while 1:
    n = int(input())
    if n == 0:
        break
    words = sorted([input() for _ in range(n)], key=str.lower)
    print(words[0])


