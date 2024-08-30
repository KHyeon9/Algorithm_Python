g, s, c = map(int, input().split())

total = g * 3 + s * 2 + c
card, treasure = "", ""

if total >= 8:
    card = "Province"
elif total >= 5:
    card = "Duchy"
elif total >= 2:
    card = "Estate"

if total >= 6:
    treasure = "Gold"
elif total >= 3:
    treasure = "Silver"
elif total >= 0:
    treasure = "Copper"

print(f"{card} or {treasure}" if card != "" else treasure)