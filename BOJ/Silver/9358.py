from collections import deque

for t in range(1, int(input()) + 1):
    n = int(input())
    nums = deque(list(map(int, input().split())))

    while len(nums) != 2:
        temp = deque()
        while nums:
            front = nums.popleft()
            if nums:
                back = nums.pop()
                temp.append(front + back)
            else:
                temp.append(front * 2)
        nums = temp

    res = "Alice" if nums[0] > nums[1] else "Bob"
    print(f"Case #{t}: {res}")