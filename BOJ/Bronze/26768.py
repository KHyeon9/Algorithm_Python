s = input()
dic = {'a': 4, 'e': 3, 'i': 1, 'o': 0, 's': 5}

for i in s:
    if i in dic:
        print(dic[i], end='')
    else:
        print(i, end='')