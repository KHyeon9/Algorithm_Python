n, m = map(int, input().split())
time = m / n * 1440
print(f"{int(time // 60):02d}:{int(time % 60):02d}")
