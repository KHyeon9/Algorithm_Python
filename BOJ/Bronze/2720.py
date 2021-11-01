n = int(input())

for i in range(n):
    m = int(input())

    q1 = m // 25
    d1 = m % 25 // 10
    n1 = m % 25 % 10 // 5
    p1 = m % 25 % 10 % 5 // 1

    print(q1, d1, n1, p1)