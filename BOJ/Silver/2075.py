import heapq
n = int(input())
heap = []
for _ in range(n):
    nums = list(map(int, input().split()))
    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    else:
        for num in nums:
            if num > heap[0]:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

print(heapq.heappop(heap))