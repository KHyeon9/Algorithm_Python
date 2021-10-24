n = int(input())
m = int(input())
x = list(map(int, input().split()))
if m == 1:
    print(n)
else:
    height = x[0]
    for i in range(m):
        if i == m - 1:
            height2 = n - x[i]
        else:
            light_range = x[i + 1] - x[i]
            if light_range % 2:
                height2 = light_range // 2 + 1
            else:
                height2 = light_range // 2
        height = max(height, height2)
    print(height)
