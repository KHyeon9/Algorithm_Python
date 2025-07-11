def solution(n, arr):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    if (arr[i] - arr[j]) / arr[k] != (arr[i] - arr[j]) // arr[k]:
                        return False
    return True

n = int(input())
nums = list(map(int, input().split()))

print("yes" if solution(n, nums) else "no")
