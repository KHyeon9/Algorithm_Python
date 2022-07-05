def convert(N, base):
    nums = "0123456789ABCDEF"
    answer = ""
    while N > 0:
        answer += nums[N % base]
        N //= base
    return answer[::-1]


for _ in range(int(input())):
    a, n = map(int, input().split())
    res = convert(a, n)
    print(1 if res == res[::-1] else 0)
