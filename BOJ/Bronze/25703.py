n = int(input())
print("int a;")
print("int *ptr = &a;")
for i in range(2, n + 1):
    if i == 2:
        print("int " + "*" * i + f"ptr{i} = &ptr;")
        continue
    print("int " + "*" * i + f"ptr{i} = &ptr{i - 1};")