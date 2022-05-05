while 1:
    player = [[0, i] for i in range(10001)]
    n, m = map(int, input().split())
    if n == m == 0:
        break

    for _ in range(n):
        nums = list(map(int, input().split()))
        for i in nums:
            player[i][0] += 1
    player.sort(reverse=True)
    second_player = [player[1][1]]
    second_score = player[1][0]
    for i in range(2, 10001):
        if player[i][0] == second_score:
            second_player.append(player[i][1])
        else:
            break
    second_player.reverse()
    print(*second_player)
