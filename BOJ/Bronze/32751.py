n = int(input())
burger = list(map(int, input().split()))
line = input()

# 빵이 처음과 마지막에 들어있지 않은 경우
if line[0] != 'a' or line[-1] != 'a':
    print("No")
    exit()

# 이전 재료와 같은 경우
for i in range(1, len(line)):
    if line[i] == line[i - 1]:
        print("No")
        exit()

# 갯수가 맞지 않는 경우
for alpa in ["a", "b", "c", "d"]:
    if line.count(alpa) > burger[ord(alpa) - ord("a")]:
        print("No")
        exit()

print("Yes")