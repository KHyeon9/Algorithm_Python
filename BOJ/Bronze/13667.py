while True:
    n = int(input())

    if n == 0:
        break
    arr = []

    for _ in range(n):
        marking = list(map(int, input().split()))
        res = [i for i in range(5) if marking[i] <= 127]

        if len(res) == 1:
            print(chr(res[0] + 65))
        else:
            print("*")