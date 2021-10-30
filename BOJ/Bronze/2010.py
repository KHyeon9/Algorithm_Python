import sys
n = int(sys.stdin.readline())
r = 0

for i in range(n):
    a = int(sys.stdin.readline())
    r += a

print(r - n + 1)