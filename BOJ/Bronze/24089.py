n, m = map(int, input().split())
box = [i for i in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    box[x] = y

for n in box[1:]:
    print(n)
