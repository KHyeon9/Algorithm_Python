n = int(input())
points = list(map(int, input().split()))
# 내림차순으로 정렬하면 짝수일 경우 alice가 항상이기고 홀수의 경우 bob이 이김
print("Alice" if n % 2 == 0 else "Bob")