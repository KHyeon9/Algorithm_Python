n = int(input())
time = int(input())
total = (time // n) * n + n - 1

print(time // n if total <= time else time // n - 1)
