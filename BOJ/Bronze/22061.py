for _ in range(int(input())):
    a, b, c = map(int, input().split())

    if c % 2 == 1 and a == 0:
        print("NO")
        continue

    print("YES" if a + b * 2 >= c else "NO")