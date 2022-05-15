duck = "quack"
s = input()

if len(s) % 5 != 0:
    print(-1)

else:
    visited = [False] * len(s)
    cnt, p = 0, 0

    for i in range(len(s)):
        if s[i] == 'q' and not visited[i]:
            flag = True
            for j in range(len(s)):
                if not visited[j] and duck[p % 5] == s[j]:
                    visited[j] = True
                    if s[j] == 'k' and flag:
                        cnt += 1
                        flag = False
                    p += 1

    if not all(visited) or cnt == 0:
        print(-1)
    else:
        print(cnt)
