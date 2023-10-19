rules = [input() for _ in range(int(input()))]

for _ in range(int(input())):
    r = int(input())
    res = "No such rule"

    if 0 <= r - 1 < len(rules):
        res = rules[r - 1]

    print(f"Rule {r}: {res}")
