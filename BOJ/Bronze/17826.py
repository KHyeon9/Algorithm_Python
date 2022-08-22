grade = [0]
grade += list(map(int, input().split()))
hongik = int(input())

res = grade.index(hongik)

if res < 6:
    print("A+")
elif res < 16:
    print("A0")
elif res < 31:
    print("B+")
elif res < 36:
    print("B0")
elif res < 46:
    print("C+")
elif res < 49:
    print("C0")
else:
    print("F")