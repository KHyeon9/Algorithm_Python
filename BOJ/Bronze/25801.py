s = input()
setString = set(list(s))

res = -1

for i in setString:
    if s.count(i) % 2 == res:
        continue

    if res != s.count(i) % 2 and res == -1:
        res = s.count(i) % 2

    else:
        res = "0/1"
print(res)
