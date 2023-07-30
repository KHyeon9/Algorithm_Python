dic = {}
res = ""
for _ in range(int(input())):
    w, b = input().split()
    dic[b] = w

s = input()

for i in range(0, len(s), 4):
    word = s[i:i+4]

    if word in dic:
        res += dic[word]
    else:
        res += "?"

print(res)