n = int(input())
before, after = list(input()), list(input())

for _ in range(n):
    for i in range(len(before)):
        if before[i] == '0':
            before[i] = '1'
        else:
            before[i] = '0'
print("Deletion succeeded" if before == after else "Deletion failed")