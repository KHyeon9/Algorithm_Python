t = int(input())

for i in range(t):
    l = list(map(int, input().split()))
    l1 = max(l) ** 2
    l.remove(max(l))
    l2 = max(l) ** 2 + min(l) ** 2
    print("Scenario #%d:" % (i + 1))
    if l1 == l2:
        print("yes")
    else:
        print("no")
    print()