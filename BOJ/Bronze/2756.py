def score(num):
    if num <= 3:
        return 100
    elif num <= 6:
        return 80
    elif num <= 9:
        return 60
    elif num <= 12:
        return 40
    elif num <= 15:
        return 20
    return 0


for _ in range(int(input())):
    dart = list(map(float, input().split()))
    player1, player2 = 0, 0
    for i in range(0, 6, 2):
        pos = dart[i] ** 2 + dart[i + 1] ** 2
        player1 += score(pos ** 0.5)
    for i in range(6, 12, 2):
        pos = dart[i] ** 2 + dart[i + 1] ** 2
        player2 += score(pos ** 0.5)
    if player1 == player2:
        print(f"SCORE: {player1} to {player2}, TIE.")
    elif player1 > player2:
        print(f"SCORE: {player1} to {player2}, PLAYER 1 WINS.")
    elif player1 < player2:
        print(f"SCORE: {player1} to {player2}, PLAYER 2 WINS.")
