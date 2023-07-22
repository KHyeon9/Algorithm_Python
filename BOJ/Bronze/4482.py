num = 0
arr = [0]
for i in range(1, 1000):
    num += i
    arr.append(arr[i - 1] + num)

for i in range(int(input())):
    n = int(input())
    print(f"{i + 1}: {n} {arr[n]}")