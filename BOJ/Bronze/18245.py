result = []
cnt = 2
while 1:
    s = input()
    if s == "Was it a cat I saw?":
        break
    line = ""
    for i in range(0, len(s), cnt):
        line += s[i]
    result.append(line)
    cnt += 1

for i in result:
    print(i)