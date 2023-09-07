rgb_list = [list(map(int, input().split())) for _ in range(16)]

while True:
    r, g, b = map(int, input().split())

    if r == g == b == -1:
        break

    rgb_list.sort(
        key=lambda x:
        ((r-x[0]) ** 2) + ((g-x[1]) ** 2) + ((b - x[2]) ** 2)
    )
    print(f"({r},{g},{b}) maps to ({rgb_list[0][0]},{rgb_list[0][1]},{rgb_list[0][2]})")