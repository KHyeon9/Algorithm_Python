cake = [8, 8, 4, 1, 9]
topping = [1, 30, 25, 10]
for _ in range(int(input())):
    empty = input()
    make_cake = list(map(int, input().split()))
    now_topping = list(map(int, input().split()))
    min_cnt = 1000000

    for i in range(5):
        n = round(make_cake[i] / cake[i], 3)
        if min_cnt > n:
            min_cnt = n
    total_cake = int(min_cnt * 16)
    total_topping = 0
    for i in range(4):
        total_topping += now_topping[i] // topping[i]
    print(min(total_topping, total_cake))
