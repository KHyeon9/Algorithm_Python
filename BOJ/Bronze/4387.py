# 2개 알파벳의 거리 계산
def calc(ch1, ch2):
    ch1_num = ord(ch1)
    ch2_num = ord(ch2)

    if ch1_num <= ch2_num:
        dist = ch2_num - ch1_num
    else:
        dist = 26 - ch1_num + ch2_num
    return dist

while True:
    line = input()
    # 탈출 조건
    if line == '#':
        break
    # 단어 따로 저장
    word1, word2, word3 = line.split()
    res = ""
    # 단어마다 계산
    for i in range(len(word1)):
        # 알파벳 거리 계산
        word_dist = calc(word1[i], word2[i])
        # 해당 거리에 따른 알파벳 위치 구하기
        char_conv = ord(word3[i]) + word_dist
        # z의 ord 값은 122
        if 122 < char_conv:
            # a의 ord 값은 97
            char_conv = (char_conv % 122) + 96
        # 변화된 위치의 알파벳으로 변환
        res += chr(char_conv)
    print(line + " " + res)