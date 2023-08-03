def get_measure_cnt(num):
    set_num = set()
    for i in range(1, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            set_num.add(i)
            set_num.add(num // i)

    return len(set_num)


while True:
    n, m = map(int, input().split())
    max_cnt = 0
    max_num = 0
    if n == m == 0:
        break

    for i in range(n, m):
        now_cnt = get_measure_cnt(i)
        if max_cnt <= now_cnt:
            max_cnt = now_cnt
            max_num = i

    print(max_num, max_cnt)
