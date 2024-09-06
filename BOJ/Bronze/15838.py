t = 1

while True:
    n = int(input())

    if n == 0:
        break

    res = 0

    for _ in range(n):
        c, b, l, n = map(int, input().split())

        c_kg, b_kg, l_kg = c / 85, b / 85, l / 85
        res += c * 0.8 + b + l * 1.2 + n * 0.8
        res -= (15.5 * c_kg + 32 * b_kg + 40 * l_kg + 0.2 * n)


    print(f"Case #{t}: RM{res:0.2f}")
    t += 1