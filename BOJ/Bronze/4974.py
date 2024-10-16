while True:
    n = int(input())

    if n == 0:
        break

    score = sorted([int(input()) for _ in range(n)])[1:-1]
    print(sum(score) // len(score))
