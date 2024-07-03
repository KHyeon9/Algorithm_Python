for _ in range(int(input())):
    n = int(input())
    arr = [0]
    for i in range(1, n + 1):
        arr.append(arr[-1] + i)
    print(sum(arr))