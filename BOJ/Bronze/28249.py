peppers = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}

res = 0

for _ in range(int(input())):
    res += peppers[input()]

print(res)