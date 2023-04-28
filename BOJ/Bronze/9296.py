for t in range(int(input())):
    n = int(input())
    answer = input()
    test_input = input()
    res = 0

    for  i in range(n):
        if answer[i] != test_input[i]:
            res += 1
    print(f"Case {t + 1}: {res}")