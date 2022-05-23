import sys
input = sys.stdin.readline

a, b = input().split()
cnt = 0
x, r1, r2 = 0, 0, 0

for i in range(2, 37):
    try:
        a_int = int(a, i)
    except:
        continue
    for j in range(2, 37):
        try:
            b_int = int(b, j)
            if i == j:
                continue
            if a_int == b_int:
                cnt += 1
                r1 = i
                r2 = j
                x = a_int
        except:
            continue

if cnt == 0:
    print("Impossible")
elif cnt == 1:
    print(x, r1, r2)
else:
    print("Multiple")