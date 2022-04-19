from sys import stdin
n, k = map(int, stdin.readline().split())
day_tem = list(map(int, stdin.readline().split()))
arr = [sum(day_tem[:k])]
for i in range(1, n - k + 1):
    n_day = arr[-1] - day_tem[i - 1] + day_tem[i + k - 1]
    arr.append(n_day)

print(max(arr))