a = list(map(int, input().split()))
b = list(map(int, input().split()))
A, B = 0, 0
for i in range(10):
    if a[i] > b[i]:
        A += 1
    elif a[i] < b[i]:
        B += 1
win = max(A, B)
if A == B:
    print('D')
elif A == win:
    print('A')
elif B == win:
    print('B')