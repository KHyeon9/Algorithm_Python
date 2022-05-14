def sol(s, target):
    l = len(old_name)
    for start in range(l):
        if s[start] == target[0]:
            for end in range(start, l):
                if s[end] == target[-1]:
                    gap = (end - start) // (len(target) - 1)
                    i = 0
                    while i < len(target):
                        if s[start + i * gap] == target[i]:
                            i += 1
                        elif s[start + i * gap] != target[i]:
                            break
                    else:
                        return 1
    return 0


n = int(input())
name = input()
result = 0
for _ in range(n):
    old_name = input()
    result += sol(old_name, name)
print(result)


