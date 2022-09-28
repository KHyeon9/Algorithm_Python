for i in range(int(input())):
    li = list(map(int, input().split()))
    if i == 0:
        print("Gnomes:")
    if li == sorted(li) or li == sorted(li, reverse=True):
        print("Ordered")
    else:
        print("Unordered")