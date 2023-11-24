n = int(input())
name = input()
k = int(input())

if name == "annyong":
    if k % 2 == 1:
        print(k)
    else:
        print(k + 1 if k + 1 <= n else k - 1)

else:
    if k % 2 == 0:
        print(k)
    else:
        print(k + 1 if k + 1 <= n else k - 1)