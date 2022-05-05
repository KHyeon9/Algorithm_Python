a = int(input())
t = int(input())
b = int(input())
game = []
cnt, i = 0, 0
while game.count(b) < t:
    game += [0, 1, 0, 1]
    for _ in range(i + 2):
        game.append(0)
    for _ in range(i + 2):
        game.append(1)
    i += 1

for i in range(len(game)):
    if game[i] == b:
        cnt += 1
    if cnt == t:
        print(i % a)
        break


