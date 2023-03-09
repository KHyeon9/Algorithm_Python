def vFor(num):
    for i in range(num - 1, 0, -1):
        print(' ' * (num - i - 1) + '*' + ' ' * (i * 2 - 1) + '*')
    print(' ' * (num - 1) + '*')

nums = list(map(int, input().split()))

for n in nums:
    vFor(n)