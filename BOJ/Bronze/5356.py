alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())

for _ in range(n):
    num, word = input().split()
    num, word = int(num), ord(word)

    for i in range(num):
        index = (word + i) % 65 % 26
        print(alpa[index] * (i + 1))
    print()