n = int(input())
times = list(map(int, input().split()))
total_time = sum(times) + 8 * (n - 1)

print(total_time // 24, total_time % 24)
