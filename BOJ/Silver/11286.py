import heapq
from sys import stdin
heap = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        if n > 0:
            heapq.heappush(heap, [n, n])
        else:
            heapq.heappush(heap, [-n, n])
