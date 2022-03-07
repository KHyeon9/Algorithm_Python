dict = {'.': '.', 'O': 'O', '-': '|',
        '|': '-', '/': '\\', '\\': '/',
        '^': '<', '<': 'v', 'v': '>',
        '>': '^'}
n, m = map(int, input().split())
box = [input() for _ in range(n)]
result = []
for i in range(m - 1, -1, -1):
    arr = []
    for j in range(n):
        arr.append(dict[box[j][i]])
    result.append(arr)
for i in result:
    print(*i, sep='')
