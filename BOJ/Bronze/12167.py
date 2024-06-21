for t in range(1, int(input()) + 1):
    s_max, audience = input().split()
    s_max = int(s_max)

    cnt, res = int(audience[0]), 0

    for level in range(1, s_max + 1):
        if cnt < level:
            res += level - cnt
            cnt = level
        cnt += int(audience[level])

    print(f"Case #{t}: {res}")