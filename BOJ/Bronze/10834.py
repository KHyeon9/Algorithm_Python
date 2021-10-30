r = 1
num = 0
for i in range(int(input())):
    a, b, c = map(int, input().split())
    r = r // a * b
    if c == 1:
        if num == 1:
            num = 0
        else:
            num = 1

print(num, r)