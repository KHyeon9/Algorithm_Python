from math import gcd


def mul(arr):
    answer = 1
    for i in range(len(arr)):
        answer *= arr[i]
    return answer


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
result = str(gcd(mul(a), mul(b)))
if len(result) > 9:
    print(result[-9:])
else:
    print(result)
