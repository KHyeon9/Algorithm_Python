t = int(input())

for i in range(t):
    a = input().split()
    r = "NO"

    if int(a[0]) + int(a[2]) == int(a[4]) and a[1] == '+':
        r = "YES"
    if int(a[0]) - int(a[2]) == int(a[4]) and a[1] == '-':
        r = "YES"

    print("Case {}: {}".format(i + 1, r))