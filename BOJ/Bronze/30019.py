from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
# 각 관마다 범위를 받는 리스트 생성
arr = [[1e9, 0] for _ in range(n)]

for _ in range(m):
    # s가 작은 순서로 들어옴
    # 따라서 각 입력마다 범위 안의 값이 아니면 범위 min, max로 수정
    k, s, e = map(int, input().split())
    # 현재 사용중인 사간 범위 가져옴
    now_s, now_e = arr[k - 1][0], arr[k - 1][1]
    
    # 시작 시간과 끝나는 시간이 범위 안에 있으면 NO 출력
    if (now_s < s < now_e) or (now_s < e < now_e):
        print("NO")
        continue
        
    # 범위 안에 속하지 않으면 범위 변경
    arr[k - 1][0] = min(s, now_s)
    arr[k - 1][1] = max(e, now_e)
    print("YES")


