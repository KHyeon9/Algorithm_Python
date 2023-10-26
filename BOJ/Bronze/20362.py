n, submitted = input().split()
n = int(n)
li = []

for _ in range(n):
    name, chat = input().split()
    if name == submitted:
        answer = chat
    li.append([name, chat])

res = 0

for i in range(n):
    if li[i][1] == answer and li[i][0] != submitted:
        res += 1

    if li[i][0] == submitted:
        print(res)
        break




