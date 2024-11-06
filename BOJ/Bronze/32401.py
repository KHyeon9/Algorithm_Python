n = int(input())
s = input()
n_cnt, res = 0, 0

for i in range(n):
    if s[i] == "A":
        for j in range(i + 1, n):
            if s[j] == "A":
                if n_cnt == 1:
                    res += 1
                break
            elif s[j] == "N":
                n_cnt += 1
    n_cnt = 0
print(res)
