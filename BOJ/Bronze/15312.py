arr = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
s = input()
s2 = input()
couple = []
for i in range(len(s)):
    name = ord(s[i]) - 65
    name2 = ord(s2[i]) - 65
    couple.append(arr[name])
    couple.append(arr[name2])
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




