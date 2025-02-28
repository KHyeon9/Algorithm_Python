import sys

def solution(n):
    answer = []
    for i in range(1, n):
        if n % i == 0:
            answer.append(i)
    return answer

nums = list(map(int, sys.stdin.read().split()))

for num in nums:
    if num == 0:
        break

    sum_list = sum(solution(num))

    if sum_list == num:
        res = "PERFECT"
    elif sum_list < num:
        res = "DEFICIENT"
    else:
        res = "ABUNDANT"

    print(f"{num} {res}")