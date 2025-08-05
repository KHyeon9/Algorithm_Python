# 문자열 값의 합을 계산해 알파벳 위치 구하는 함수
def decode(string):
    n = 0
    for ch in string:
        n += ord(ch) - ord('a')
    return n % 27

alpa = "abcdefghijklmnopqrstuvwxyz "

for _ in range(int(input())):
    line = list(input().split())
    res = ""
    for el in line:
        # 구한 문자를 저장
        res += alpa[decode(el)]
    print(res)