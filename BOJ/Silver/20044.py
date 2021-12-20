n = int(input())
students = list(map(int, input().split()))
teams = []
for i in range(n):
    r = max(students) + min(students)
    teams.append(r)
    students.remove(max(students))
    students.remove(min(students))
print(min(teams))

