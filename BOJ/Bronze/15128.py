p1, q1, p2, q2 = map(int, input().split())

r1 = p1 * p2
r2 = 2 * q1 * q2

print(r1 % r2 == 0 and 1 or 0)
