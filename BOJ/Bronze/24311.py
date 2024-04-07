t1, t2 = map(int, input().split())
t3 = int(input())
t4, t5 = map(int, input().split())
br = int(input())
t6 = int(input())

res = t1 * 60 + t2 - (t3 + t4 * 60 + t5 + (br + 1) * t6 + 10)

print(f"{res // 60:02} {res % 60:02}")