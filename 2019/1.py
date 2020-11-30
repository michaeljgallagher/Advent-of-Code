with open('1.txt', 'r') as file:
    data = file.readlines()
data = [int(x) for x in data]


def fuel_required(mass):
    return int(mass/3) - 2


total = 0
for module in data:
    total += fuel_required(module)
print(total)  # 3358992


def fuel2(mass):
    res = 0
    fuel = fuel_required(mass)
    res += fuel
    while fuel > 6:
        fuel = fuel_required(fuel)
        res += fuel
    return res


total = 0
for module in data:
    total += fuel2(module)
print(total)  # 5035632
