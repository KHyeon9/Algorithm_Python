for _ in range(int(input())):
    a, b = input().split()
    result = []
    for i in range(len(a)):
        r = ord(b[i]) - ord(a[i])
        if a[i] > b[i]:
            r += 26
        result.append(r)
    print('Distances:', *result)
