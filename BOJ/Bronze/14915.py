def convert(num, base):
    nums = "0123456789ABCDEF"
    answer = ""
    while num > 0:
        answer += nums[num % base]
        num //= base
    return answer[::-1]

m, n = map(int, input().split())
if m == 0:
    print(0)
    exit()
print(convert(m, n))