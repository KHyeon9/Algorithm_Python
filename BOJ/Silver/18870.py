n = int(input())
x = list(map(int, input().split()))
X = sorted(list(set(x)))
dic = {X[i]: i for i in range(len(X))}
for i in x:
    print(dic[i], end=' ')
