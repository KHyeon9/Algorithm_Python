n = int(input())
for _ in range(n):
    car_num = input().split('-')
    alpha = car_num[0]
    num = int(car_num[1])
    Sum = num
    for i in range(len(alpha)):
        Sum -= (ord(alpha[-i - 1]) - 65) * (26 ** i)

    if abs(Sum) <= 100:
        print("nice")
    else:
        print("not nice")