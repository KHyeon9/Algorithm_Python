korea = "KOREA"

s = input()
res = ""

for w in s:
    if korea[len(res) % 5] == w:
        res += w

print(len(res))