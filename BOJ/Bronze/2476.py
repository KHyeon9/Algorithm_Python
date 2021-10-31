n = int(input())
r = []

for i in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        r.append(a * 1000 + 10000)

    elif a == b or a == c:
        r.append(a * 100 + 1000)

    elif b == c:
        r.append(b * 100 + 1000)

    else:
        r.append(max(a, b, c) * 100)

print(max(r))