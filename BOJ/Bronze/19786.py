for _ in range(int(input())):
    a, c = map(int, input().split())
    r, g, b = map(int, input().split())

    red = a * ((r + 1) ** 2 + g ** 2 + b ** 2) + c * min(r + 1, g, b)
    green = a * (r ** 2 + (g + 1) ** 2 + b ** 2) + c * min(r, g + 1, b)
    blue = a * (r ** 2 + g ** 2 + (b + 1) ** 2) + c * min(r, g, b + 1)

    if green <= red >= blue:
        print("RED")
    elif red <= green >= blue:
        print("GREEN")
    else:
        print("BLUE")