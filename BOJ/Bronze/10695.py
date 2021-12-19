for i in range(int(input())):
    n, r1, c1, r2, c2 = map(int, input().split())
    r = abs(r1 - r2) + abs(c1 - c2)
    if r == 3:
        print(f"Case {i + 1}: YES")
    else:
        print(f"Case {i + 1}: NO")