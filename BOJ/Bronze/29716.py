j, n = map(int, input().split())
res = 0
for _ in range(n):
    s = input()
    point = 0
    for w in s:
        if w.isupper():
            point += 4
        elif w.islower() or w.isdigit():
            point += 2
        elif w == " ":
            point += 1

    if point <= j:
        res += 1
print(res)
