while True:
    grade = sorted(list(map(int, input().split())))

    if sum(grade) == 0:
        break

    grade = grade[1:-1]
    res = sum(grade) / len(grade)
    print(int(res) if res == int(res) else res)