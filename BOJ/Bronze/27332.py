month = 11

day = int(input())
weeks = int(input())

day += 7 * weeks

print(1 if day <= 30 else 0)
