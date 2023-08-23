t_room, t_cond = map(int, input().split())
air_cord_mode = input()

if air_cord_mode == "freeze":
    res = min(t_room, t_cond)
elif air_cord_mode == "heat":
    res = max(t_room, t_cond)
elif air_cord_mode == "auto":
    res = t_cond
else:
    res = t_room

print(res)