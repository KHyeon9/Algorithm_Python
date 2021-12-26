n = int(input())
r = 0

for i in range(n):
    n1, n2 = map(int, input().split())

    r += n2 - (n1 * (n2 // n1))

print(r)