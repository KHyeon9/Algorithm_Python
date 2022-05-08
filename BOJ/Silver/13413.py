for _ in range(int(input())):
    n = int(input())
    o1 = input()
    o2 = input()
    arr = []
    for i in range(n):
        if o1[i] != o2[i]:
            arr.append(o1[i])
    if arr.count('W') > arr.count('B'):
        print(arr.count('W'))
    else:
        print(arr.count('B'))