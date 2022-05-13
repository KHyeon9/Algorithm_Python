alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cnt = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
dic = {}
total = 0
for i in range(len(alpha)):
    dic[alpha[i]] = cnt[i]

s = input()
for word in s:
    total += dic[word]

print("I'm a winner!" if total % 2 == 1 else "You're the winner?")
