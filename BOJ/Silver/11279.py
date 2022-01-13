import heapq
from sys import stdin
n = int(stdin.readline())
heap = []
for i in range(n):
    num = int(stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap) * -1)
    else:
        heapq.heappush(heap, -num)
