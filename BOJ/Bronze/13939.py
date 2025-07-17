n = int(input())
s = input()
start, li = 0, []

for i in range(len(s)):
    if s[i] in [".", "?", "!"]:
        li.append(s[start:i].split())
        i += 2
        start = i

for el in li:
    cnt = 0
    for w in el:
        if w[0].isupper() and w.isalpha():
            cnt += 1
    print(cnt)