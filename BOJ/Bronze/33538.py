l = int(input())
n = int(input())
t = float(input())
flag = False

for _ in range(n):
    f, b = map(float, input().split())
    time = l / f + l / b
    if t > time:
        flag = True

print("HOPE" if flag else "DOOMED")