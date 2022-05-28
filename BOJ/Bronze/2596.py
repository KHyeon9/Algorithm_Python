pa = ["000000", "001111", "010011",
      "011100", "100110", "101001",
      "110101", "111010"]
alpa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
n = int(input())
messages = input()
message_cut = [messages[i * 6:i * 6 + 6] for i in range(n)]
res = ""
pos = 0
for mes in message_cut:
    no = 0
    for p in pa:
        cnt = 0
        for i in range(6):
            if mes[i] == p[i]:
                cnt += 1
            else:
                pos = max(pos, cnt)
        if cnt >= 5:
            res += alpa[pa.index(p)]
            break
        else:
            no += 1
    if no == 8:
        print(message_cut.index(mes) + 1)
        exit()
print(res)