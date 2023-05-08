max_score = [0, 51, 180]
res_index = 0

for i in range(int(input())):
    s, c, l = map(int, input().split())
    if s > max_score[0] or (s == max_score[0] and c < max_score[1]) or (
            s == max_score[0] and c == max_score[1] and l < max_score[2]):
        max_score = [s, c, l]
        res_index = i

print(res_index + 1)
