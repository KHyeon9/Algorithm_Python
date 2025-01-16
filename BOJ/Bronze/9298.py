for t in range(int(input())):
    n = int(input())
    x_list, y_list = [], []

    for _ in range(n):
        x, y = map(float, input().split())
        x_list.append(x)
        y_list.append(y)

    x_max, x_min = max(x_list), min(x_list)
    y_max, y_min = max(y_list), min(y_list)
    x_len = x_max - x_min
    y_len = y_max - y_min

    print(f"Case {t + 1}: Area {x_len * y_len}, Perimeter {(x_len + y_len) * 2}")
