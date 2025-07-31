line = input().split()
res = [word for word in line if word not in ["bubble", "tapioka"]]
print(" ".join(res) if res else "nothing")