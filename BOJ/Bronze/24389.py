n = int(input())
# 2진수로 변환하고 32 길이로 변환
bin_n = bin(n)[2:].zfill(32)
res = 0
twos_complement = ""
# 비트 반전
for ch in bin_n:
    twos_complement += "0" if ch == "1" else "1"
# 1 더하기
twos_complement = bin(int(twos_complement, 2) + 1)[2:]
# 각 자리마다 숫자가 다른 경우 계산
for i in range(32):
    if bin_n[i] != twos_complement[i]:
        res += 1
print(res)