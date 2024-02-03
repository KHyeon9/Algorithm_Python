from collections import defaultdict

while True:
    n = int(input())

    if n == 0:
        break

    medal_cnt = defaultdict(int)
    gold_medal_cnt = defaultdict(int)

    for _ in range(n):
        year, event, medal_color = input().split()

        medal_cnt[year] += 1

        if medal_color == "Gold":
            gold_medal_cnt[year] += 1

    res = [0, 0]
    max_gold = 0

    for t in sorted(gold_medal_cnt.items()):
        year = t[0]
        if max_gold < gold_medal_cnt[year]:
            max_gold = gold_medal_cnt[year]
            res[0] = year

    max_medal = 0
    for t in sorted(medal_cnt.items()):
        year = t[0]
        if max_medal < medal_cnt[year]:
            max_medal = medal_cnt[year]
            res[1] = year

    print(*res)


