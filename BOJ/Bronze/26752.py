h, m, s = map(int, input().split())

total = h * 3600 + m * 60 + s + 1
hr = total // 3600 % 24
mr = total % 3600 // 60
sr = total % 60

print(f"{str(hr).zfill(2)}:{str(mr).zfill(2)}:{str(sr).zfill(2)}")
