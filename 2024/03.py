import re

with open("03.txt", "r") as file:
    data = file.read().strip()


def part_one(s):
    return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", s))


def part_two(s):
    res = 0
    do = True
    i = j = 0
    for match in re.finditer(r"mul\((\d+),(\d+)\)", s):
        j = match.span()[0]
        if "do()" in s[i:j]:
            do = True
        if "don't()" in s[i:j]:
            do = False
        if do:
            res += int(match.group(1)) * int(match.group(2))
        i = j
    return res


print(f"Part 1: {part_one(data)}")
print(f"Part 2: {part_two(data)}")
