rating_list = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
         "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0,
         "F": 0}

res_score, res_cnt = 0, 0

for _ in range(20):
    subject, grade, rating = input().split()

    if rating == "P":
        continue

    res_score += float(grade) * rating_list[rating]
    res_cnt += float(grade)

print(round(res_score / res_cnt, 6))