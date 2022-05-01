def dfs(start):
    visited[start] = True

    for i in range(1, test_case[0]):
        if not visited[i] and graph[start][i] == 1:
            dfs(i)


for _ in range(int(input())):
    test_case = list(map(int, input().split()))
    visited = [False] * (test_case[0])
    graph = [[0] * (test_case[0]) for _ in range(test_case[0])]
    for i in range(2, test_case[1] * 2 + 1, 2):
        a, b = test_case[i], test_case[i + 1]
        graph[a][b] = 1
        graph[b][a] = 1
    dfs(0)
    if False not in visited:
        print("Connected.")
    else:
        print("Not connected.")