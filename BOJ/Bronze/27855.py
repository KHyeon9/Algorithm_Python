h1, b1 = map(int, input().split())
h2, b2 = map(int, input().split())

p1_point = 3 * h1 + b1
p2_point = 3 * h2 + b2

if p1_point > p2_point:
    res = f"1 {p1_point - p2_point}"
elif p2_point > p1_point:
    res = f"2 {p2_point - p1_point}"
else:
    res = "NO SCORE"
print(res)