T = int(input())
arr = [[10], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]

for i in range(T):
    a, b = map(int, input().split())
    a = a % 10

    if a == 1 or a == 5 or a == 6 or a == 0:
        print(arr[a][0])

    elif a == 4 or a == 9:
        print(arr[a][b % 2])

    else:
        print(arr[a][b % 4])
