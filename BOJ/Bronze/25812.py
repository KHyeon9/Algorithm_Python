n, r = map(int, input().split())
static, double = 0, 0
for _ in range(n):
    num = int(input())
    if num > r:
        double += 1

    elif num < r:
        static += 1


if double < static:
    print(1)
elif double > static:
    print(2)
else:
    print(0)