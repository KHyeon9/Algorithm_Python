n = int(input())
up = 7
r = 5

for i in range(0, n - 1):
    r += up
    up += 3

print(r % 45678)