a = list(map(int, input().split()))
b = list(map(int, input().split()))
p1 = 0
p2 = 0
last_w = 0

for i in range(10):
    if a[i] > b[i]:
        p1 += 3
        last_w = 1
    elif a[i] < b[i]:
        p2 += 3
        last_w = 0
    else:
        p1 += 1
        p2 += 1

if p1 == p2:
    if p1 == 10:
        w = 'D'
    else:
        if last_w == 1:
            w = 'A'
        elif last_w == 0:
            w = 'B'
else:
    if p1 > p2:
        w = 'A'
    else:
        w = 'B'

print(p1, p2)
print(w)