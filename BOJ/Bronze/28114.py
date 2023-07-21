team_name = [list(input().split()) for _ in range(3)]
problem_sort = sorted(team_name, key=lambda x: int(x[0]))[::-1]
year_sort = sorted(team_name, key=lambda x: int(x[1]))
name1 = ""
name2 = ""

for y in year_sort:
    name1 += y[1][2:]

for p in problem_sort:
    name2 += p[2][0]
print(name1)
print(name2)
