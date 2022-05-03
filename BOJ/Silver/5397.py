n = int(input())
for _ in range(n):
    line = input()
    result = []
    stack = []
    for i in range(len(line)):
        if line[i] == '<':
            if result:
                stack.append(result.pop())
        elif line[i] == '>':
            if stack:
                result.append(stack.pop())
        elif line[i] == '-':
            if result:
                result.pop()
        else:
            result.append(line[i])
    result.extend(reversed(stack))
    print(*result, sep='')
