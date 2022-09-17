import json
import re

with open("12.txt", "r") as file:
    raw_data = file.read().strip()


def parse_json(j):
    match j:
        case dict():
            return 0 if "red" in j.values() else sum(map(parse_json, j.values()))
        case list():
            return sum(map(parse_json, j))
        case int():
            return j
        case _:
            return 0


def part_one():
    return sum(map(int, re.findall(r"(-?\d+)", raw_data)))


def part_two():
    j = json.loads(raw_data)
    return parse_json(j)


print(f"Part 1: {part_one()}")  # 111754
print(f"Part 2: {part_two()}")  # 65402
