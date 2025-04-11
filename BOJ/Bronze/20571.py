def solution(section, num):
    if section == "residential":
        if num == 1:
            return 1
        elif 2 <= num < 6:
            return 1
        elif 6 <= num < 11:
            return 2
        elif 11 <= num < 16:
            return 3
        return 4
    elif section == "commercial":
        if num == 1:
            return 0
        elif 2 <= num < 8:
            return 1
        elif 8 <= num < 15:
            return 2
        return 3
    else:
        if num == 1:
            return 0
        elif 2 <= num < 5:
            return 1
        elif 5 <= num < 9:
            return 2
        elif 9 <= num < 13:
            return 3
        elif 13 <= num < 17:
            return 4
        return 5

s, n = input().split()
n = int(n)

print(solution(s, n))