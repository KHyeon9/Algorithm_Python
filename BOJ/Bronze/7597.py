while True:
    s = input()

    if s == "#":
        break
    score_res = {"A": 0, "B": 0}
    score = [0, 0]
    for w in s:
        score[ord(w) - ord('A')] += 1

        if max(score) >= 4:
            if abs(score[0] - score[1]) >= 2:
                res = chr(score.index(max(score)) + ord('A'))
                score_res[res] += 1
                score = [0, 0]

    print(f"A {score_res['A']} B {score_res['B']}")
