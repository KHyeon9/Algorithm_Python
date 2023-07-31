def isfloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


for _ in range(int(input())):
    test_case = input()
    flag = True
    if isfloat(test_case):
        if float(test_case) % 1 != 0 or float(test_case) < 0:
            flag = False
    else:
        flag = False

    print(int(test_case) if flag else "invalid input")
