bin_total = ""

for _ in range(3):
    bin_num = bin(int(input()))[2:]
    # 길이 검사
    if len(bin_num) < 4:
        bin_num = "0" * (4 - len(bin_num)) + bin_num
    # 4-lsb 적용
    bin_total += bin_num[-4:]
# 10진수로 변경
res = str(int(bin_total, 2))
# 길이가 4 이하일 경우 앞에 0 추가
print("0" * (4 - len(res)) + res)
