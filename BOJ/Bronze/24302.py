def solution(d):
    km = d // 1000

    if km <= 5:
        first = 400
    elif 5 < km <= 10:
        first = 700
    elif 10 < km <= 20:
        first = 1200
    elif 20 < km <= 30:
        first = 1700
    else:
        first = 57 * km

    if km <= 2:
        second = 90 + (90 * km)
    elif 2 < km <= 5:
        second = 100 + (85 * km)
    elif 5 < km <= 20:
        second = 125 + (80 * km)
    elif 20 < km <= 40:
        second = 325 + (70 * km)
    else:
        second = 925 + (55 * km)

    return min(first, second)

a, b = map(int, input().split())
total = solution(a) + solution(b)

print(f"{total // 100}.{total % 100:02d}")