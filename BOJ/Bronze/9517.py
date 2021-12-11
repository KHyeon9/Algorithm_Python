k = int(input())
n = int(input())
s = 0

for i in range(n):
    t, z = input().split()
    s += int(t)

    if s >= 210:
        r = k
        break

    if z == 'T':
        k += 1
        if k == 9:
            k = 1

print(r)