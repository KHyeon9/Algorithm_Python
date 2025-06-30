for _ in range(int(input())):
    n = int(input())
    temp = [i for i in range(1, n + 1)]
    li = list(map(int, input().split()))

    for i in range(n):
        if temp[i] == li[i]:
            temp[i] += 1

        for j in range(i + 1, n):
            if temp[j - 1] >= temp[j]:
                temp[j] += (temp[j - 1] - temp[j]) + 1
    print(temp[-1])