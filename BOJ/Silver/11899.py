s = input()
arr = []
for i in s:
    if i == '(':
        arr.append(i)
    else:
        if len(arr) != 0 and arr[-1] == '(':
            arr.pop()
        else:
            arr.append(i)
print(len(arr))