for _ in range(int(input())):
    result_r, result_g, result_b = 0, 0, 0
    for _ in range(10):
        r, g, b = map(int, input().split())
        result_r += r
        result_g += g
        result_b += b
    print(round((result_r + 0.1) / 10), round((result_g + 0.1) / 10), round((result_b + 0.1)/10))
