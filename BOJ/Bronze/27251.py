for i in range(1, int(input()) + 1):
    if i <= 10:
        print("*" * (i ** 2))
    else:
        print("*" * 100 + "...")
