with open("02.txt", "r") as file:
    data = file.read().strip()


def part_one(data):
    res = 0
    for line in data.split("\n"):
        a, b = line.split(" ")
        cur = ord(b) - ord("A") - 22
        if a == "A":
            cur += 3 if b == "X" else 6 if b == "Y" else 0
        elif a == "B":
            cur += 0 if b == "X" else 3 if b == "Y" else 6
        else:
            cur += 6 if b == "X" else 0 if b == "Y" else 3
        res += cur
    return res


def part_two(data):
    res = 0
    for line in data.split("\n"):
        a, b = line.split(" ")
        cur = (ord(b) - ord("A") - 23) * 3
        if a == "A":
            cur += 3 if b == "X" else 1 if b == "Y" else 2
        elif a == "B":
            cur += 1 if b == "X" else 2 if b == "Y" else 3
        else:
            cur += 2 if b == "X" else 3 if b == "Y" else 1
        res += cur
    return res


print(f"Part 1: {part_one(data)}")  # 13005
print(f"Part 2: {part_two(data)}")  # 11373
