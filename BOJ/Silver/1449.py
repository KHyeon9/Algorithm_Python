n, l = map(int, input().split())
pipe = sorted(list(map(int, input().split())))
now_pipe = 0
cnt = 0
for i in pipe:
    if now_pipe < i:
        cnt += 1
        now_pipe = i + l - 1
print(cnt)
