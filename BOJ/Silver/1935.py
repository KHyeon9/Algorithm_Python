n = int(input())
s = input()
nums = [int(input()) for _ in range(n)]
stack = []
for word in s:
    if word.isalpha():
        stack.append(nums[ord(word) - ord('A')])
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if word == '+':
            num = n1 + n2
            stack.append(num)
        elif word == '-':
            num = n1 - n2
            stack.append(num)
        elif word == '*':
            num = n1 * n2
            stack.append(num)
        elif word == '/':
            num = n1 / n2
            stack.append(num)
print("%.2f" % stack[0])