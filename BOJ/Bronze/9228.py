while True:
    num = input()

    if num == "#":
        break

    total, mul = 0, 2

    for n in num[::-1]:
        total += int(n) * mul
        mul += 1

    temp = total % 11
    check_digit = 11 - temp

    if check_digit == 10:
        res = "Rejected"
    elif check_digit == 11:
        res = "0"
    else:
        res = str(check_digit)

    print(f"{num} -> {res}")



