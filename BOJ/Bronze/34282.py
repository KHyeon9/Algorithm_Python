def solution(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

x, y, z = map(int, input().split())
avg = x * 0.25 + y * 0.25 + z * 0.5
print(solution(avg))