n = int(input())
ox = input()
bonus, result = 0, 0

for i in range(n):
    if ox[i] == 'O':
        result += i + 1 + bonus
        bonus += 1

    else:
        bonus = 0
print(result)
