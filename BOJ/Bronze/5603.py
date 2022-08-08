n = int(input())
num = input()
res = ""
for _ in range(n):
    N = ""
    cnt = 1
    word = num[0]
    for i in num[1:]:
        if i != word:
            N += str(cnt) + word
            cnt = 1
            word = i
        else:
            cnt += 1
    if cnt != 0:
        N += str(cnt) + word
    num = N
print(num)
