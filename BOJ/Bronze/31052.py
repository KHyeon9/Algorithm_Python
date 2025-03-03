n, q = map(int, input().split())
company_point = [0] + list(map(int, input().split()))

for _ in range(q):
    a, c, x = map(int, input().split())

    if a == 1:
        company_point[c] = x
    else:
        print(abs(company_point[c] - company_point[x]))

