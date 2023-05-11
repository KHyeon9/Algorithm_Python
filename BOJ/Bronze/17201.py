n = int(input())
mag = input()
flag = True
for i in range(2, n * 2, 2):
    if mag[i] == mag[i - 1]:
        flag = False
        break

print('Yes' if flag else 'No')