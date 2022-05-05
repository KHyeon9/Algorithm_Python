n = int(input())
files = [list(input().split('.')) for _ in range(n)]
files_cnt = {}
for file in files:
    files_cnt[file[1]] = 0

for i in files:
    files_cnt[i[1]] += 1
file_cnt = sorted(files_cnt.items())

for file_name, file_cnt in file_cnt:
    print(file_name, file_cnt)