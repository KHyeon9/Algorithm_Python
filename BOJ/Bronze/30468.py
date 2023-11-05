line = list(map(int, input().split()))
n = line[-1]
total_stat = sum(line[:-1])
res = n * 4 - total_stat
print(res if res > 0 else 0)