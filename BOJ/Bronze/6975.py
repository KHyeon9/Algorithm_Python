for _ in range(int(input())):
    n = int(input())
    measure = []

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            measure.append(i)

    sum_measure = sum(measure)
    res = "is a perfect number."
    if sum_measure > n:
        res = "is an abundant number."
    elif sum_measure < n:
        res = "is a deficient number."

    print(f"{n} {res}")
    print()