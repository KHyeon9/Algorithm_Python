for _ in range(int(input())):
    n, m = map(int, input().split())
    vote = [0] * n
    for _ in range(m):
        rangeCnt = list(map(int, input().split()))
        for i in range(n):
            vote[i] += rangeCnt[i]
    print(vote.index(max(vote)) + 1)
