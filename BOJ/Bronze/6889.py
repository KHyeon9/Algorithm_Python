n = int(input())
m = int(input())
adjectives = [input() for _ in range(n)]
nouns = [input() for _ in range(m)]

for i in adjectives:
    for j in nouns:
        print(f"{i} as {j}")