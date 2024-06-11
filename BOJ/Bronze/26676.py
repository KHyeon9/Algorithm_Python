def solution(n, words):
    arr = {
        1: [0, 0, 0],
        2: [0, 0, 0],
        3: [0, 0, 0],
        4: [0, 0, 0],
        5: [0, 0, 0]
    }

    for w in words:
        num, word = int(w[0]), ord(w[1]) - ord('A')
        arr[num][word] += 1

    for el in arr:
        cut = 1 if el != 5 else 2

        for i in range(3):
            if arr[el][i] < cut:
                return "NIE"
    return "TAK"


n = int(input())
words = list(input().split())

print(solution(n, words))