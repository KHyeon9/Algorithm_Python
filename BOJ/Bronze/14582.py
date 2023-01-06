je = list(map(int, input().split()))
st = list(map(int, input().split()))
je_total, st_total = 0, 0
flag = False

for i in range(9):
    je_total += je[i]
    if je_total > st_total:
        flag = True
    st_total += st[i]
if flag and je_total < st_total:
    print("Yes")
else:
    print("No")