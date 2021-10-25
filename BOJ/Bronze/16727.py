a, b = map(int, input().split())
c, d = map(int, input().split())

r1 = a + d
r2 = b + c

if r1 > r2:
    print("Persepolis")

elif r1 < r2:
    print("Esteghlal")

else:
    if a > c:
        print("Esteghlal")

    elif a < c:
        print("Persepolis")

    else:
        print("Penalty")