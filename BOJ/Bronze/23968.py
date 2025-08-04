from sys import stdin

# 버블 정렬
def bubble_sort(n, arr, k):
    cnt = 0
    for i in range(n - 1, 0, -1):
        for j in range(i):
            # 두수 비교후 교환
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cnt += 1
                # k번째 교환시 값 출력
                if cnt == k:
                    print(arr[j], arr[j + 1])
                    return
    print(-1)

N, K = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
bubble_sort(N, nums, K)
