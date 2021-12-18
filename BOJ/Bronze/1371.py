import sys
arr = [0] * 27
s = sys.stdin.read()
for i in s:
    if i.islower():
        arr[ord(i) - 97] += 1
for j in range(27):
    if arr[j] == max(arr):
        print(chr(j + 97), end='')

