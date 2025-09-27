s = int(input())
d = float(input())
t = float(input())
conv = s *(5280 / 3600) * t
print("MADE IT" if d <= conv else "FAILED TEST")