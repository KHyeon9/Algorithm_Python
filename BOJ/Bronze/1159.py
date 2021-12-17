arr = [0] * 27
result = []
for _ in range(int(input())):
    s = input()
    arr[ord(s[0]) - 97] += 1
for i in range(27):
    if arr[i] >= 5:
        result.append(chr(i + 97))
if len(result) == 0:
    print('PREDAJA')
else:
    print(''.join(result))
