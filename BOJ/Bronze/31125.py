for _ in range(int(input())):
    s, n, f, m = map(int, input().split())
    min_num = n + m
    max_num = f * n + m

    print("YES" if min_num <= s <= max_num else "NO")