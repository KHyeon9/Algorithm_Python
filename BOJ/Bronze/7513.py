for case in range(1, int(input()) + 1):
    n = int(input())
    words = [input() for _ in range(n)]
    # case 출력
    print(f"Scenario #{case}:")

    for _ in range(int(input())):
        # password에 사용될 words의 인덱스 입력
        pwd_idxs = list(map(int, input().split()))
        password = ""
        # 해당 인덱스에 맞는 word를 가져와 password 구성
        for idx in pwd_idxs[1:]:
            password += words[idx]
        print(password)
    print()