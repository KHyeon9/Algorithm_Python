for _ in range(int(input())):
    cards = list(input().split())

    total_cards = {
        'A': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
        '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0,
        'Q': 0, 'K': 0
    }

    for c in cards:
        total_cards[c[0]] += 1

    max_value = max(total_cards, key=total_cards.get)
    print(total_cards[max_value])

