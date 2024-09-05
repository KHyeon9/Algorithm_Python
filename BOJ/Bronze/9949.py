t = 1
while True:
    words = list(input().split())

    if words[0] == words[1] == '#':
        break
    print(f"Case {t}")
    for _ in range(int(input())):
        line = list(input())

        for i in range(len(line)):
            if line[i].lower() in words:
                line[i] = '_'

        print(*line, sep='')
    print()
    t += 1