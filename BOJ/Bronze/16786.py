n = int(input())
pieces = list(map(int, input().split()))
m = int(input())
pos = list(map(int, input().split()))

for n in pos:
    n = n - 1
    if pieces[n] + 1 not in pieces:
        pieces[n] += 1

    if pieces[n] > 2019:
        pieces[n] = 2019
for i in pieces:
    print(i)