isbn = input()
total = 0
star_idx = isbn.index("*")

for i in range(len(isbn)):
    if i == star_idx:
        continue
    total += int(isbn[i]) if i % 2 == 0 else int(isbn[i]) * 3

for n in range(10):
    weight = 1 if star_idx % 2 == 0 else 3
    if (total + n * weight) % 10 == 0:
        print(n)
        break
