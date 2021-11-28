t = int(input())

for i in range(t):
    t2 = int(input())
    a = []
    for j in range(t2):
        n = int(input())
        if n < 6:
            a.append(n + 1)
    print(f"Case {i + 1}:")
    for j in range(len(a)):
        print(a[j])