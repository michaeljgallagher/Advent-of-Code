import re

with open("03.txt", "r") as file:
    data = file.read().strip()


def part_one(s):
    return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", s))


def part_two(s):
    res = 0
    do = True
    for match in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", s):
        if match.group(0) == "do()":
            do = True
        elif match.group(0) == "don't()":
            do = False
        elif do:
            res += int(match.group(1)) * int(match.group(2))
    return res


print(f"Part 1: {part_one(data)}")
print(f"Part 2: {part_two(data)}")
