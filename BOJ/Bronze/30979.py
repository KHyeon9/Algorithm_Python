t = int(input())
n = int(input())
f_list = list(map(int, input().split()))

print("Padaeng_i Happy" if sum(f_list) >= t else "Padaeng_i Cry")