a = int(input())

M = a // 5
m = a % 5

if m != 0:
    M += 1

print(M)