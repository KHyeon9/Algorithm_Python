n, m = map(int, input().split())
cards = list(map(int, input().split()))
card_front = cards[:n]
card_back = cards[n:]
now_card = cards[:n]

for _ in range(m):
    k = int(input())
    for i in range(n):
        if now_card[i] <= k:
            if now_card[i] == card_front[i]:
                now_card[i] = card_back[i]
            else:
                now_card[i] = card_front[i]
print(sum(now_card))
