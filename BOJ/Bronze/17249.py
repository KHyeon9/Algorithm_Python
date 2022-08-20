teabo = input()
flag = False
left, right = 0, 0
for i in teabo:
    if i == '(':
        flag = True

    if i == '@' and not flag:
        left += 1
    elif i == '@' and flag:
        right += 1
print(left, right)