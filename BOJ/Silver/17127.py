n = int(input())
tree = list(map(int, input().split()))
res = 0

def solution(start, end):
    li = tree[start:end]
    answer = 1

    for el in li:
        answer *= el

    return answer

for i in range(1, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            total = solution(0, i) + solution(i, j) + solution(j, k) + solution(k, n)
            res = max(res, total)
print(res)