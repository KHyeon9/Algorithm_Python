num = input()
# 2진법으로 바꿔서 배열에 저장
arr = [bin(int(n))[2:].zfill(4) for n in num]

for i in range(4):
    line = []
    for j in range(4):
        # 0인 경우 . 아닌 경우 *
        bit = "*" if arr[j][i] == "1" else "."
        line.append(bit)
    print(f"{line[0]} {line[1]}   {line[2]} {line[3]}")
