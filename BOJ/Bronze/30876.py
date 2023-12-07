res_x, res_y = 0, 1e9
for _ in range(int(input())):
    x, y = map(int, input().split())
    if res_y > y:
        res_x, res_y = x, y

print(res_x, res_y)