def solution(l):
    places = [
        [200, 210, 220], [210, 220, 225], [220, 225, 230],
        [225, 230, 235], [230, 235, 245], [235, 245, 250],
        [260, 265, 270], [265, 270, 275], [270, 275, 280],
        [275, 280, 285], [280, 285, 290], [285, 290, 295],
        [290, 295, 300]
    ]
    cnts = [500, 300, 100]
    answer = [0] * 13

    for i in range(13):
        for j in range(3):
            if places[i][j] <= l:
                answer[i] = cnts[j]
    return answer

level = int(input())
res = solution(level)

print(*res[:6])
print(*res[6:])