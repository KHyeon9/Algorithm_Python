n = int(input())
levels = [int(input()) for _ in range(n)][::-1]
result = 0

for i in range(n - 1):
    if levels[i] <= levels[i + 1]:
        result += levels[i + 1] - levels[i] + 1
        levels[i + 1] = levels[i] - 1
print(result)