n = int(input())
books = {}

for _ in range(n):
    book = input()

    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

max_cnt = max(books.values())
res_books = []

for k, v in books.items():
    if v == max_cnt:
        res_books.append(k)

print(sorted(res_books)[0])