x_list = []
y_list = []

for i in range(int(input())):
    x, y = map(int, input().split(','))
    x_list.append(x)
    y_list.append(y)

print(f"{min(x_list) - 1},{min(y_list) - 1}")
print(f"{max(x_list) + 1},{max(y_list) + 1}")
