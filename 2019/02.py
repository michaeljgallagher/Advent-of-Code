with open('02.txt', 'r') as file:
    data = file.read()
data = data.split(',')
data = [int(x) for x in data]
data_copy = data[:]


def opcode(lst):
    i = 0
    while lst[i] != 99:
        if lst[i] == 1:
            lst[lst[i+3]] = lst[lst[i+1]] + lst[lst[i+2]]
        elif lst[i] == 2:
            lst[lst[i+3]] = lst[lst[i+1]] * lst[lst[i+2]]
        i += 4
    return lst


# replace position 1 with the value 12 and replace position 2 with the value 2
data[1] = 12
data[2] = 2

# What value is left at position 0 after the program halts?
opcode(data)
print(data[0])  # 3654868

data = data_copy[:]


def part2():
    for i in range(100):
        for j in range(100):
            data = data_copy[:]
            data[1] = i
            data[2] = j
            opcode(data)
            if data[0] == 19690720:
                return i, j


print(part2())  # 70, 14 (answer is 7014)
