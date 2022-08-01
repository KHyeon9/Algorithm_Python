for _ in range(int(input())):
    t, w = map(float, input().split())
    bmi = w / (t ** 2 / 10000)
    if t <= 140.1:
        print(6)
    elif 140.1 <= t < 146:
        print(5)
    elif 146 <= t < 159:
        print(4)
    elif 159 <= t < 161:
        if 16 <= bmi < 35:
            print(3)
        else:
            print(4)
    elif 161 <= t < 204:
        if 20 <= bmi < 25:
            print(1)
        elif 18.5 <= bmi < 20 or 25 <= bmi < 30:
            print(2)
        elif 16 <= bmi < 18.5 or 30 <= bmi < 35:
            print(3)
        else:
            print(4)
    else:
        print(4)