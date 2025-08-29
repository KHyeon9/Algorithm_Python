# 거울에 의한 반전값
def mirror(num):
    if num == "2":
        return "5"
    elif num == "5":
        return "2"
    elif num == "1" or num == "8":
        return num
    else:
        return "?"

w, n = input().split()
n = int(n)
original = [list(input().split()) for _ in range(n)]
res = [["0"] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 반전에 따른 조건
        if w == "L" or w == "R":
            res[i][n - j - 1] = mirror(original[i][j])
        else:
            res[n - i - 1][j] = mirror(original[i][j])
for el in res:
    print(*el)

