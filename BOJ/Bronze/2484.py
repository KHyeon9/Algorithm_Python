max_total = 0
for _ in range(int(input())):
    total = 0
    dice = sorted(list(map(int, input().split())))
    if len(set(dice)) == 1:
        total += 50000 + dice[0] * 5000
    elif len(set(dice)) == 2:
        max_dice = 0
        min_dice = 7
        for i in set(dice):
            if dice.count(i) == 3:
                total += 1000 * i + 10000
                break
            if dice.count(i) == 2:
                max_dice = max(max_dice, i)
                min_dice = min(min_dice, i)
        if max_dice != 0 and min_dice != 7:
            total += 2000 + 500 * (max_dice + min_dice)
    elif len(set(dice)) == 3:
        for i in set(dice):
            if dice.count(i) == 2:
                total += 1000 + 100 * i
                break
    elif len(set(dice)) == 4:
        total += max(dice) * 100
    max_total = max(max_total, total)

print(max_total)
