for _ in range(int(input())):
    cost = 0
    result = ''
    for _ in range(int(input())):
        c, name = input().split()
        if int(c) > cost:
            cost = int(c)
            result = name
    print(result)