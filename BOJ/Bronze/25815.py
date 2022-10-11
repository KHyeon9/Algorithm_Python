y, m = map(int, input().split())
age_year = 0
age_month = 0

if y < 1:
    age_year += (15 * m) // 12
    age_month += (15 * m) % 12
elif y == 1:
    age_year += 15 + (9 * m) // 12
    age_month += (9 * m) % 12
else:
    age_year += 24 + (y - 2) * 4 + ((4 * m) // 12)
    age_month += (4 * m) % 12
print(age_year, age_month)

