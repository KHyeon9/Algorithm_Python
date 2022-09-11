# 우리는 dnalaeZ gnimmargorP tsetnoC no .ht4에 나타납니다.
# 나는 아이스크림을 좋아한다.

while 1:
    line = list(input().split())
    res = []
    if line[0] == '#':
        break

    for i in line:
        res.append(i[::-1])
    print(*res)