n, c = map(int, input().split())
fireflower = [int(input()) for _ in range(n)]
time = [0] * (c + 1)

for fire in fireflower:
    for i in range(1, c + 1):
        if i % fire == 0:
            time[i] += 1
result = c - time.count(0) + 1
print(result)