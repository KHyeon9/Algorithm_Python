answer = [(i - 1) % 5 + 1 for i in range(1, 11)]
result = []
for i in range(int(input())):
    student = list(map(int, input().split()))
    if answer == student:
        result.append(i + 1)
for r in result:
    print(r)