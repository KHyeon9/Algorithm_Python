num = input()

nums_list = []

while True:
    l = len(num)

    if l > 2:
        middle_pointer = l // 2
        middle_num = int(num[middle_pointer - 1:middle_pointer + 1])
        num = str(middle_num ** 2)
    else:
        if l == 1:
            num = '0'
        else:
            num = str(int(num[0]) ** 2)

    if num in nums_list:
        nums_list.append(num)
        break
    nums_list.append(num)

print(len(nums_list))
