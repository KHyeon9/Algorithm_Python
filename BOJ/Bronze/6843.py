line1 = input().replace(" ", "")
line2 = input().replace(" ", "")
flag = False

if len(line1) == len(line2):
    count1 = [0] * 27
    count2 = [0] * 27

    for i in range(len(line1)):
        idx1 = ord(line1[i]) - ord('A')
        idx2 = ord(line2[i]) - ord('A')
        count1[idx1] += 1
        count2[idx2] += 1

    if count1 == count2:
        flag = True

print("Is an anagram." if flag else "Is not an anagram.")
