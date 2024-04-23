date = [[3, 21], [4, 20], [5, 21], [6, 21], [7, 23],
        [8, 23], [9, 23], [10, 23], [11, 23], [12, 22],
        [1, 20], [2, 19]]
constellation = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius",
    "Pisces"
]

y, m, d = map(int, input().split("-"))

for i in range(12):
    day = m * 30 + d
    start = date[i][0] * 30 + date[i][1]
    end = date[(i + 1) % 12][0] * 30 + date[(i + 1) % 12][1]

    if start > end and (start <= day or end > day):
        print(constellation[i])
        break
    elif start <= day < end:
        print(constellation[i])
        break