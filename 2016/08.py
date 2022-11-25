import re

with open("08.txt", "r") as file:
    data = file.read().strip()

RECT = re.compile(r"rect (\d+)x(\d+)")
ROT_ROW = re.compile(r"rotate row y=(\d+) by (\d+)")
ROT_COL = re.compile(r"rotate column x=(\d+) by (\d+)")


def rect(screen, x, y):
    for i in range(y):
        screen[i][:x] = ["#"] * x
    return screen


def rotate_row(screen, y, by):
    screen[y] = screen[y][-by:] + screen[y][:-by]
    return screen


def rotate_col(screen, x, by):
    col = [screen[i][x] for i in range(len(screen))]
    col = col[-by:] + col[:-by]
    for i in range(len(screen)):
        screen[i][x] = col[i]
    return screen


def make_screen(data):
    screen = [[" "] * 50 for _ in range(6)]
    for command in data.split("\n"):
        if m := re.match(RECT, command):
            screen = rect(screen, int(m.group(1)), int(m.group(2)))
        elif m := re.match(ROT_ROW, command):
            screen = rotate_row(screen, int(m.group(1)), int(m.group(2)))
        elif m := re.match(ROT_COL, command):
            screen = rotate_col(screen, int(m.group(1)), int(m.group(2)))
    return screen


SCREEN = make_screen(data)


def part_one():
    return sum(row.count("#") for row in SCREEN)


def part_two():
    return "\n" + "\n".join("".join(row) for row in SCREEN)


print(f"Part 1: {part_one()}")  # 106
print(f"Part 2: {part_two()}")  # CFLELOYFCS
