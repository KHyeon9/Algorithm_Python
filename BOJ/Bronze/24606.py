password = input()
inputPassword = input()

cnt = 0

for i in range(4):
    if password[i] == inputPassword[i]:
        cnt += 1

print(2 ** (4 - cnt))