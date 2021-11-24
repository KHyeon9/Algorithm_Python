s = input()
key = input()
s2 = ''
num = '0123456789'
for i in s:
    if i not in num:
        s2 += i
if key in s2:
    print(1)
else:
    print(0)