def solution(n):
    if n < 0.2:
        return "weak"
    elif n < 0.4:
        return "normal"
    elif n < 0.6:
        return "strong"
    return "very strong"

px, pr = map(int, input().split())
print(solution(px / pr))
