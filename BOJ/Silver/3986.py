n = int(input())
cnt = 0
for _ in range(n):
    s = input()
    stack = []
    for word in s:
        if stack and stack[-1] == word:
            if stack[-1] == word:
                stack.pop()
        else:
            stack.append(word)

    if not stack:
        cnt += 1
print(cnt)