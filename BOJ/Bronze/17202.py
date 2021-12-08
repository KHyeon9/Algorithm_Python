s = input()
s2 = input()
couple = []
for i in range(len(s)):
    couple.append(int(s[i]))
    couple.append(int(s2[i]))
while 1:
    dp = []
    if len(couple) == 2:
        break
    for i in range(len(couple) - 1):
        num = couple[i] + couple[i + 1]
        if num >= 10:
            num -= 10
        dp.append(num)
    couple = dp
print(f'{couple[0]}{couple[1]}')