ottawa = int(input())

print(f"{ottawa} in Ottawa")

victoria = ottawa - 300 if ottawa - 300 >= 0 else ottawa + 2100
print(f"{victoria} in Victoria")

edmonton = ottawa - 200 if ottawa - 200 >= 0 else ottawa + 2200
print(f"{edmonton} in Edmonton")

winnipeg = ottawa - 100 if ottawa - 100 >= 0 else ottawa + 2300
print(f"{winnipeg} in Winnipeg")

print(f"{ottawa} in Toronto")

halifax = (ottawa + 100) % 2400
print(f"{halifax} in Halifax")

st_johns_h = ottawa // 100
st_johns_m = ottawa % 100

st_johns_h += 1
st_johns_m += 30

if st_johns_m >= 60:
    st_johns_m -= 60
    st_johns_h += 1

print(f"{(st_johns_h * 100 + st_johns_m) % 2400} in St. John's")
