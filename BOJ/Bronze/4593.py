while True:
    player1 = input()
    player2 = input()
    res_p1, res_p2 = 0, 0

    if player1 == player2 == 'E':
        break

    for i in range(len(player1)):
        if player1[i] == 'R' and player2[i] == 'S':
            res_p1 += 1
        elif player1[i] == 'S' and player2[i] == 'P':
            res_p1 += 1
        elif player1[i] == 'P' and player2[i] == 'R':
            res_p1 += 1
        elif player1[i] == 'S' and player2[i] == 'R':
            res_p2 += 1
        elif player1[i] == 'P' and player2[i] == 'S':
            res_p2 += 1
        elif player1[i] == 'R' and player2[i] == 'P':
            res_p2 += 1

    print(f"P1: {res_p1}")
    print(f"P2: {res_p2}")