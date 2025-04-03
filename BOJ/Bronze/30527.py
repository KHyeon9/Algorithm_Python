al = list(map(int, input().split()))
n, kwf = map(int, input().split())
total = 0

for i in range(0, 10, 2):
    total += al[i] * al[i + 1]

res = total // 5 * n // kwf
print(res)