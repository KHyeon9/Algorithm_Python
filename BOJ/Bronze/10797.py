n = int(input())
c = list(map(int, input().split()))
r = 0

for i in range(5):
    if c[i] == n:
        r += 1

print(r)
