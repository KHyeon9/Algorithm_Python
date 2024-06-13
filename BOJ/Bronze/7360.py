while True:
    n = int(input())

    if n == 0:
        break

    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    res_a, res_b = 0, 0

    for i in range(n):
        if abs(a_list[i] - b_list[i]) == 1:
            if a_list[i] < b_list[i]:
                if b_list[i] == 2:
                    res_a += 6
                else:
                    res_a += a_list[i] + b_list[i]
            else:
                if a_list[i] == 2:
                    res_b += 6
                else:
                    res_b += a_list[i] + b_list[i]

        elif a_list[i] > b_list[i]:
            res_a += a_list[i]
        elif a_list[i] < b_list[i]:
            res_b += b_list[i]

    print(f"A has {res_a} points. B has {res_b} points.\n")
