for _ in range(int(input())):
    arr = []
    t = int(input())
    flag = False
    for _ in range(t):
        s = input()
        arr.append(s)
    for i in range(t):
        for j in range(t):
            if i == j:
                continue
            r = arr[i] + arr[j]
            if r == r[::-1]:
                print(r)
                flag = True
                break
        if flag:
            break
    if not flag:
        print(0)