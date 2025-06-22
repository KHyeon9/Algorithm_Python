n, l, h = map(int, input().split())
score = sorted(list(map(int, input().split())))
print(sum(score[l:n - h]) / (n - l - h))