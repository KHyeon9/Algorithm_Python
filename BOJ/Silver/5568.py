from itertools import permutations
n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
cards_p = list(permutations(cards, k))
result = []
for num in cards_p:
    N = int("".join(num))
    if N not in result:
        result.append(N)
print(len(result))
