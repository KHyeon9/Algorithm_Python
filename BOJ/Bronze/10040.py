n, m = map(int, input().split())
vote = [0] * n
cost = [int(input()) for _ in range(n)]

for _ in range(m):
    p = int(input())
    for i in range(n):
        if cost[i] <= p:
            vote[i] += 1
            break
print(vote.index(max(vote)) + 1)