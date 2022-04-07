a, b, c = map(int, input().split())
if a != b == c:
    print('A')
elif a != b != c:
    print('B')
elif a == b != c:
    print('C')
else:
    print('*')