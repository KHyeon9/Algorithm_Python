res = 0

for _ in range(int(input())):
    s = input()
    cnt = s.count("for") + s.count("while")
    res = max(cnt, res)

print(res)
