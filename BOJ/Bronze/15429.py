for i in range(int(input())):
    h, m = map(int, input().split())
    total = h * 60 + m - 45

    if total < 0:
        total += 24 * 60

    print(f"Case #{i + 1}: {total // 60} {total % 60}")