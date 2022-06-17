n, m = map(int, input().split())
box = sum(list(map(int, input().split())))
book = sum(list(map(int, input().split())))
print(box - book)
