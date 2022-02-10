from sys import stdin
read = stdin.readline
sang = ['A', 'B', 'C']
chang = ['B', 'A', 'B', 'C']
hyun = ['C', 'C', 'A', 'A', 'B', 'B']
n = int(read())
answer = read()
r1, r2, r3 = 0, 0, 0
for i in range(n):
    if answer[i] == sang[i % 3]:
        r1 += 1
    if answer[i] == chang[i % 4]:
        r2 += 1
    if answer[i] == hyun[i % 6]:
        r3 += 1
print(max(r1, r2, r3))
if r1 == max(r1, r2, r3):
    print('Adrian')
if r2 == max(r1, r2, r3):
    print('Bruno')
if r3 == max(r1, r2, r3):
    print('Goran')