def solution(arr, x, y):
    dx = [0, 1, 0, 1]
    dy = [0, 0, 1, 1]
    nums = []

    for idx in range(4):
        mx = x + dx[idx]
        my = y + dy[idx]
        num = arr[mx][my]
        nums.append(num)
    nums.sort()
    return nums[-2]


n = int(input())
cnn = [list(map(int, input().split())) for _ in range(n)]

while len(cnn) != 1:
    a = []
    for i in range(0, len(cnn), 2):
        temp = []
        for j in range(0, len(cnn), 2):
            temp.append(solution(cnn, i, j))
        a.append(temp)
    cnn = a
print(*cnn[0])
