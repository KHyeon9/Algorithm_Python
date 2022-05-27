while 1:
    study = list(input().split())
    cnt = 0
    if study[0] == '#':
        break
    for i in study[1:]:
        cnt += i.lower().count(study[0])
    print(study[0], cnt)


