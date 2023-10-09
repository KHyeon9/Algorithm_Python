for t in range(int(input())):
    n = int(input())
    res_round = "Round 1"

    if n <= 25:
        res_round = "World Finals"
    elif n <= 1000:
        res_round = "Round 3"
    elif n <= 4500:
        res_round = "Round 2"

    print(f"Case #{t + 1}: {res_round}")