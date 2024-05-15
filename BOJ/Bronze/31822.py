subject = input()[:5]
res = 0

for _ in range(int(input())):
    retake = input()[:5]

    if subject == retake:
        res += 1

print(res)