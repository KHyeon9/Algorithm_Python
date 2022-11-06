t = int(input())
studnet_answer = [input() for _ in range(t)]
cnt = 0
for i in range(t):
    test_answer = input()
    if studnet_answer[i] == test_answer or test_answer == '_':
        cnt += 1
print(cnt)