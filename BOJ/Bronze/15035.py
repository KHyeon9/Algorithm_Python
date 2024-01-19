n = int(input())
h_list = list(map(int, input().split()))
tree_h = int(input())
min_tree = 3000
res = 500

for h in h_list:
    if min_tree > tree_h % h:
        min_tree = tree_h % h
        res = h

print(res)