a_list = ["A", "D", "E"]
c_list = ["C", "F", "G"]
line = input().split("|")
c_cnt, a_cnt = 0, 0

for el in line:
    if el[0] in c_list:
        c_cnt += 1
    if el[0] in a_list:
        a_cnt += 1

if c_cnt == a_cnt:
    if line[-1][-1] in c_list:
        c_cnt += 1
    if line[-1][-1] in a_list:
        a_cnt += 1

print("C-major" if c_cnt > a_cnt else "A-minor")