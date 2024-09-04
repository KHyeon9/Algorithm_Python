min_res, max_res = 100, -100
while True:
    try:
        data = list(map(int, list(input().split())[1:]))
        min_res = min(min(data), min_res)
        max_res = max(max(data), max_res)
    except:
        break

print(f"{min_res} {max_res}")