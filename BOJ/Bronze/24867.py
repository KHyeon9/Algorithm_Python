k = int(input())
a, x = map(int, input().split())
b, y = map(int, input().split())

case1 = (k - a) * x
case2 = (k - b) * y
case3 = (k - a) * x + (k - a - b) * y
case4 = (k - b) * y + (k - a - b) * x

print(max(case1, case2, case3, case4, 0))