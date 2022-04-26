n = int(input())
files = list(map(int, input().split()))
disc = int(input())
total = 0
for file in files:
    if file % disc == 0:
        total += file // disc
    else:
        total += file // disc + 1
print(total * disc)
