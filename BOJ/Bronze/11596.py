tr1 = sorted(list(map(int, input().split())))
tr2 = sorted(list(map(int, input().split())))

if tr1[0] == tr2[0] and tr1[1] == tr2[1] and tr1[2] == tr2[2] and tr1[0] ** 2 + tr1[1] ** 2 == tr1[2] ** 2:
    print("YES")
else:
    print("NO")