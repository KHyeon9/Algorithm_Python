for _ in range(int(input())):
    s = list(map(int, input()))[::-1]
    result = 0
    for i in range(24):
        result += 2 ** i * s[i]
    print(result)