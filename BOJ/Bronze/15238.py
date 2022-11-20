n = int(input())
s = list(input())
setArr = set(s)
cnt, result = 0, ""
for i in setArr:
    if s.count(i) > cnt:
        cnt = s.count(i)
        result = i
print(result, cnt)