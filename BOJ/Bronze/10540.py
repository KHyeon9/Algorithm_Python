x_list = []
y_list = []

for _ in range(int(input())):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

res_x = max(x_list) - min(x_list)
res_y = max(y_list) - min(y_list)

print(max(res_x, res_y) ** 2)