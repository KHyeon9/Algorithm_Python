def rangeSum(list, strat, end):
    return sum(list[strat - 1: end])

def rangePow(list, start, end):
    for i in range(start - 1, end):
        list[i] = (list[i] ** 2 % 2010)

    return list

n = int(input())
a_list = list(map(int, input().split()))

for _ in range(int(input())):
    k, l, r = map(int, input().split())

    if k == 1:
        a_list = rangePow(a_list, l, r)
    else:
        print(rangeSum(a_list, l, r))