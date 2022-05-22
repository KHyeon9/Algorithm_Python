from sys import stdin

def check(arr, m):
    for i in range(m):
        if abs(arr[m] - arr[i]) == m - i:
            return False
    return True


def n_queen(arr, n, q):
    global result

    if n == q:
        result += 1
        return

    for i in range(q):
        arr[n] = i
        if visited[i]:
            continue
        if check(arr, n):
            visited[i] = True
            n_queen(arr, n + 1, q)
            visited[i] = False


N = int(stdin.readline())
chess = [0] * N
visited = [False] * N
result = 0
n_queen(chess, 0, N)
print(result)