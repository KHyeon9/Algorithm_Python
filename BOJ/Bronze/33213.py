n = int(input())
arr = list(map(int, input().split()))
odd, even = [], []

for num in arr:
    if num % 2 == 1:
        odd.append(num)
    else:
        even.append(num)

if len(odd) > len(even):
    odd.sort()
    for i in range(1, odd[-1] + 3, 2):
        if i not in odd:
            print(i)
            break
else:
    even.sort()
    for i in range(2, even[-1] + 3, 2):
        if i not in even:
            print(i)
            break
