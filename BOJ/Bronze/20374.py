import sys
input_lines = sys.stdin.readlines()

res = 0
for num in input_lines:
    n1, n2 = map(int, num.strip().split('.'))
    res += n1 * 100 + n2

print(f"{res // 100}.{res % 100:02d}")