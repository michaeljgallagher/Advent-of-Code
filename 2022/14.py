with open("14.txt", "r") as file:
    data = file.read().strip()


def parse_input(data):
    def parse_line(line):
        res = []
        for coord in line.split(" -> "):
            x, y = coord.split(",")
            res.append((int(x), int(y)))
        return res

    return [parse_line(line) for line in data.split("\n")]


def get_walls(data):
    def add_walls(x1, y1, x2, y2):
        if x1 == x2:
            return set(
                (x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)
            )
        else:
            return set(
                (x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)
            )

    walls = set()
    for lines in parse_input(data):
        for i in range(len(lines) - 1):
            x1, y1 = lines[i]
            x2, y2 = lines[i + 1]
            walls |= add_walls(x1, y1, x2, y2)
    return walls


WALLS = get_walls(data)
MAX_Y = max(y for x, y in WALLS)


def drop_sand(part_two=False):
    occupied = WALLS.copy()
    while True:
        if part_two and (500, 0) in occupied:
            return len(occupied) - len(WALLS)
        x, y = 500, 0
        while True:
            if not part_two and y == MAX_Y:
                return len(occupied) - len(WALLS)
            elif part_two and y == MAX_Y + 1:
                occupied.add((x, y))
                break
            if (x, y + 1) not in occupied:
                y += 1
            elif (x - 1, y + 1) not in occupied:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in occupied:
                x += 1
                y += 1
            else:
                occupied.add((x, y))
                break


print(f"Part 1: {drop_sand()}")  # 1406
print(f"Part 2: {drop_sand(True)}")  # 20870
