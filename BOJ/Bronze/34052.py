times = [int(input()) for _ in range(4)]
last_time = 1800 - sum(times)

print("Yes" if last_time >= 300 else "No")