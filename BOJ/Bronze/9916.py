from math import factorial

n = int(input())
# 팩토리얼로 계산 후 문자열로 변경
n_fac_str = str(factorial(n))
# 0의 갯수 세기
print(n_fac_str.count('0'))