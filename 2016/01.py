with open("01.txt", "r") as file:
    data = file.read().strip()

MOVES = [(str(x[0]), int(x[1:])) for x in data.split(", ")]
DIRS = {
    "R": 0 - 1j,
    "L": 0 + 1j,
}


def part_one():
    face, pos = 0 + 1j, 0 + 0j
    for d, blocks in MOVES:
        face *= DIRS[d]
        pos += face * blocks
    return int(abs(pos.real) + abs(pos.imag))


def part_two():
    face, pos = 0 + 1j, 0 + 0j
    seen = set()
    for d, blocks in MOVES:
        face *= DIRS[d]
        for _ in range(blocks):
            if pos in seen:
                return int(abs(pos.real) + abs(pos.imag))
            seen.add(pos)
            pos += face
    return -1


print(f"Part 1: {part_one()}")  # 209
print(f"Part 2: {part_two()}")  # 136
