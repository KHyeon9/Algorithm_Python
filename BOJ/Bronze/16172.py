s = input()
word = input()
p = 0
res = ""
for i in s:
    if i.isdigit():
        continue
    res += i
if word in res:
    print(1)
else:
    print(0)