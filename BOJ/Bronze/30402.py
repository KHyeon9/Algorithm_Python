res = ""
for _ in range(15):
    line = list(input().split())

    if "w" in line:
        res = "chunbae"
    elif "b" in line:
        res = "nabi"
    elif "g" in line:
        res = "yeongcheol"

print(res)