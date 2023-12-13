numbers = list(map(int, input()))

for i in range(16):
    if i % 2 == 0:
        change = numbers[i] * 2

        if change >= 10:
            change = change // 10 + change % 10

        numbers[i] = change

print("DA" if not sum(numbers) % 10 else "NE")
