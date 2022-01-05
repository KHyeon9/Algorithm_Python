n, m = map(int, input().split())
score = list(map(int, input().split()))
answer = []
for i in range(m):
    student = list(input().split())
    student[0] = int(student[0])
    r = 0
    for j in range(n):
        if student[j + 1] == 'O':
            r += score[j]
    answer.append([student[0], r])
answer.sort(key=lambda x: [-x[1], x[0]])
print(*answer[0])