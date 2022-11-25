import re
from collections import Counter

with open("04.txt", "r") as file:
    data = file.read().strip()

ROOMS = re.findall(r"([a-z-]+)-(\d+)\[([a-z]+)\]", data)


def part_one():
    return sum(
        int(sector)
        for name, sector, checksum in ROOMS
        if checksum
        == "".join(
            x[0]
            for x in sorted(
                Counter(name.replace("-", "")).most_common(),
                key=lambda x: (-x[1], x[0]),
            )[:5]
        )
    )


def part_two():
    return next(
        int(sector)
        for name, sector, checksum in ROOMS
        if checksum
        == "".join(
            x[0]
            for x in sorted(
                Counter(name.replace("-", "")).most_common(),
                key=lambda x: (-x[1], x[0]),
            )[:5]
        )
        and "north"
        in "".join(
            chr((ord(c) - ord("a") + int(sector)) % 26 + ord("a"))
            for c in name.replace("-", " ")
        )
    )


print(f"Part 1: {part_one()}")  # 361724
print(f"Part 2: {part_two()}")  # 482
