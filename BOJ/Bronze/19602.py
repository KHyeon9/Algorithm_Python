a = [int(input())for _ in range(3)]

r = a[0] + 2 * a[1] + 3 * a[2]

if r >= 10:
    print("happy")

else:
    print("sad")