from sys import stdin
arr = set()
for _ in range(int(stdin.readline())):
    name, log = stdin.readline().split()
    if log == 'enter':
        arr.add(name)
    else:
        arr.remove(name)
for i in sorted(arr, reverse=True):
    print(i)