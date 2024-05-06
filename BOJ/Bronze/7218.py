rome_num = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
    "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
    "XI": 11, "XII": 12
}

n = int(input())
s = input()
res = []

for num in rome_num:
    if num in s:
        res.append(rome_num[num])

print(*res)
