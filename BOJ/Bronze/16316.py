n = int(input())
nums = list(input().split())
res = "makes sense"
for i in range(n):
    if nums[i] == str(i + 1) or nums[i] == "mumble":
        continue
    else:
        res = "something is fishy"
print(res)