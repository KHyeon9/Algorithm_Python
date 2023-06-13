while True:
    player1, player2 = input().split()

    if player1 == player2 == '#':
        break

    player1_point, player2_point = 0, 0

    for _ in range(int(input())):
        coin, coin_answer = input().split()

        if coin == coin_answer:
            player1_point += 1
        else:
            player2_point += 1

    print(f"{player1} {player1_point} {player2} {player2_point}")