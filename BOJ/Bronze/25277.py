ban = ['he', 'him', 'she', 'her']
n = int(input())
line = list(input().split())
cnt = 0
for i in line:
    if i in ban:
        cnt += 1
print(cnt)