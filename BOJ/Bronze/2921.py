n = int(input())
r = 0

for i in range(n + 1):
    for j in range(i, n + 1):
        r += i + j

print(r)