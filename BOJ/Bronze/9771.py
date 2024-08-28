w = input()
res = 0

while True:
    try:
        s = input()
        res += s.count(w)
    except:
        break

print(res)