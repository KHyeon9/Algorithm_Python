n = int(input())
line = input()
# 필요한 값들 dict로 선언
chip = {"B": 0, "R": 0, "O": 0, "N": 0, "Z": 0,
        "E": 0, "S": 0, "I": 0, "L": 0, "V": 0}

for ch in line:
    if ch in chip:
        chip[ch] += 1

# E와 R은 2개씩 필요하므로 2로 나눠줌
chip["E"] = chip["E"] // 2
chip["R"] = chip["R"] // 2

# dict의 value들의 가장 작은 값을 반환
print(min(chip.values()))
