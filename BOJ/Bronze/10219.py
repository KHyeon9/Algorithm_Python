for _ in range(int(input())):
    h, w = map(int, input().split())
    meat = [input() for _ in range(h)]
    for line in meat:
        print(*line[::-1], sep='')