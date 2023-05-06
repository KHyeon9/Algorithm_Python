dic = {'STRAWBERRY': 0, 'BANANA': 0, 'LIME': 0, 'PLUM': 0}

for _ in range(int(input())):
    name, num = input().split()
    dic[name] += int(num)

for key in dic:
    if dic[key] == 5:
        print('YES')
        break
else:
    print('NO')