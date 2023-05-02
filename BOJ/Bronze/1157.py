s = input().lower()
s_set = list(set(s))
count_list = []

for w in s_set:
    count_list.append(s.count(w))

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    print(s_set[count_list.index(max(count_list))].upper())