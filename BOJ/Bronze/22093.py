for _ in range(int(input())):
    n, a, b = map(int, input().split())

    min_sol = max(0, a - b)
    max_sol = min(a, n - b)

    print(min_sol, max_sol)