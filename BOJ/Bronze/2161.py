n = int(input())
card = [i for i in range(1, n + 1)]
result = []
for i in range(n - 1):
    result.append(card[0])
    card.pop(0)
    card.append(card[0])
    card.pop(0)
result.append(card[0])
print(*result)
