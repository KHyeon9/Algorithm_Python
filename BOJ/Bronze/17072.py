# 숫자 계산
def calc(r, g, b):
    return 2126 * r + 7152 * g + 722 * b
# 해당 숫자 문자로 변경
def conv(num):
    if num < 510000:
        return "#"
    elif num < 1020000:
        return "o"
    elif num < 1530000:
        return "+"
    elif num < 2040000:
        return "-"
    else:
        return "."

n, m = map(int, input().split())

for _ in range(n):
    # 라인 입력
    line = list(map(int, input().split()))
    conv_line = ""
    # rgb를 찾아 문자로 변경
    for i in range(m):
        num = calc(
            line[3 *i], line[3 * i + 1], line[3 * i + 2]
        )
        conv_line += conv(num)

    print(conv_line)

