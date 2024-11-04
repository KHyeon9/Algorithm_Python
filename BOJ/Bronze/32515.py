n = int(input())
lines = [input() for _ in range(4)]
res = ""

for i in range(n):
    if lines[0][i] == lines[2][i]:
        if lines[1][i] == lines[3][i]:
            res += lines[1][i]
        else:
            print("htg!")
            exit()
print(res)