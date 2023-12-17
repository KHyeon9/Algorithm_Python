n = int(input())
line = input()
cnt_list = {"B": line.count("B"), "S": line.count("S"), "A": line.count("A")}
max_cnt = max(cnt_list, key=cnt_list.get)
res = ""

for cnt in cnt_list:
    if cnt_list[max_cnt] == cnt_list[cnt]:
        res += cnt

if res == "BSA":
    print("SCU")
else:
    print(res)



