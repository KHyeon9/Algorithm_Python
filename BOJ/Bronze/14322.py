for t in range(1, int(input()) + 1):
    n = int(input())
    max_len = 0
    res = ""

    for _ in range(n):
        name = input()
        name_set = set(list(name))
        name_set.discard(' ')

        if max_len < len(name_set):
            max_len = len(name_set)
            res = name
        elif max_len == len(name_set) and res > name:
            res = name


    print(f"Case #{t}: {res}")