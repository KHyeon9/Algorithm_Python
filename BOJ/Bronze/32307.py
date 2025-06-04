word_set = set()
# 중복 제거를 위한 set
for _ in range(int(input())):
    word_set.add(input())

# 이후 입력을 받음
for _ in range(int(input())):
    word = input()
    # 입력 단이가 단어 리스트에 있는 경우
    if word in word_set:
        print(1)
    else:
        flag = False
        for word2 in word_set:
            # 단어 2개를 합친 것인지 판단
            if word.startswith(word2):
                temp = word[len(word2):]
                if temp in word_set:
                    flag = True
                    break
        # 단어 2개를 합친거면 2 아니면 0
        print(2 if flag else 0)