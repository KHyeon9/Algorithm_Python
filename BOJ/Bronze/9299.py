t = int(input())

for i in range(t):
    n = list(map(int, input().split()))
    a = [n[0] - 1]
    for j in range(n[0]):
        a.append((n[0] - j) * n[j + 1])

    print(f"Case {i + 1}:", *a)