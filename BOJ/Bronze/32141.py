n, h = map(int, input().split())
cards = list(map(int, input().split()))
total = 0
for i in range(n):
    total += cards[i]
    if total >= h:
        print(i + 1)
        exit()
if total < h:
    print(-1)
