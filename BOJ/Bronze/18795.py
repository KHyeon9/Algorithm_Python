n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# 한번씩 다 거쳐야 하므로 리스트의 모든 값을 더함
print(sum(a_list) + sum(b_list))