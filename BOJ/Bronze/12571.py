for i in range(1, int(input()) + 1):
    n = int(input())

    if n == 1:
        input()
        print(f"Case #{i}: 0")
        continue

    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())

    print(f"Case #{i}:", end=" ")
    print(
        1 if (a1 > a2 and b1 < b2) or
             (a1 < a2 and b1 > b2) else 0
    )