t = 0
while True:
    n = int(input())
    t += 1

    if n < 0: break
    x_sum, y_sum, m_sum = 0, 0, 0

    for _ in range(n):
        x, y, m = map(int, input().split())

        x_sum += x * m
        y_sum += y * m
        m_sum += m

    input()

    a = round(x_sum / m_sum, 2)
    b = round(y_sum / m_sum, 2)

    print(f"Case {t}: {a:.2f} {b:.2f}")