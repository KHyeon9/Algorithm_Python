from sys import stdin
input = stdin.readline

arr = []
dict = {}

for _ in range(int(input())):
    line = list(input().split())
    arr.append(line)

# 첫 단어 정렬
arr.sort()

for el in arr:
    if el[0] in dict:
        dict[el[0]].append(el[1])
    else:
        dict[el[0]] = [el[1]]

for key in dict:
    # 두번째 단어 역순 정렬
    for el in sorted(dict[key], reverse=True):
        print(key, el)
