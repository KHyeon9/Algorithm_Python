t = int(input())
total_card_list = []
player_cards = {}

for i in range(t):
    card_list = list(map(int, input().split()))[1:]
    total_card_list += card_list
    for card in card_list:
        player_cards[card] = chr(ord('A') + i)

for card in sorted(total_card_list):
    print(player_cards[card], end="")
