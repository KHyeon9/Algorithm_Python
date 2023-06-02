n, q = map(int, input().split())
nums = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        print(sum(nums[query[1]-1:query[2]]))
        nums[query[1]-1], nums[query[2]-1] = nums[query[2]-1], nums[query[1]-1]
    else:
        first = sum(nums[query[1]-1:query[2]])
        second = sum(nums[query[3]-1:query[4]])
        print(first - second)
