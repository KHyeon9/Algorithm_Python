a, b = map(int, input().split())
arr = set(map(int, input().split()))
arr2 = set(map(int, input().split()))
r = []
for i in arr:
    if i not in arr2:
        r.append(i)
print(len(r))
if len(arr) != 0:
    print(*sorted(r))
else:
    print(0)