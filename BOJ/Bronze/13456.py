for _ in range(int(input())):
    n = int(input())
    v_list = list(map(int, input().split()))
    u_list = list(map(int, input().split()))
    res = 0

    for i in range(n):
        if v_list[i] != u_list[i]:
            res += 1

    print(res)
