n = int(input())
arr = list(map(int, input().split()))
arr_sort = sorted(arr)

for i in arr:
    print(arr_sort.index(i) + 1)