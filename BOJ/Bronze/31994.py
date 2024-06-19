dic = {}

for _ in range(7):
    name, cnt = input().split()
    dic[name] = int(cnt)

print(max(dic, key=dic.get))
