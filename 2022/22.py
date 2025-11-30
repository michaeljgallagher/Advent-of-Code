import re


def parse_input():
    with open("22.txt", "r") as file:
        data = file.read()
    grid_text, path_text = data.split("\n\n")
    lines = grid_text.split("\n")
    grid = {}
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char in ".#":
                grid[(r, c)] = char
    path = []
    for match in re.finditer(r"(\d+|[LR])", path_text):
        token = match.group(1)
        if token.isdigit():
            path.append(int(token))
        else:
            path.append(token)
    return grid, path


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def turn(facing, direction):
    if direction == "R":
        return (facing + 1) % 4
    else:
        return (facing - 1) % 4


def wrap_2d(grid, r, c, dr, dc):
    if dr != 0:
        if dr > 0:
            nr = min(i for i, j in grid if j == c)
        else:
            nr = max(i for i, j in grid if j == c)
        return nr, c
    else:
        if dc > 0:
            nc = min(j for i, j in grid if i == r)
        else:
            nc = max(j for i, j in grid if i == r)
        return r, nc


def get_cube_faces(grid):
    total_tiles = len(grid)
    face_size = int((total_tiles // 6) ** 0.5)
    return None, None, face_size


def wrap_cube(row, col, facing, face_size):
    face_r = row // face_size
    face_c = col // face_size
    local_r = row % face_size
    local_c = col % face_size

    if facing == 0:  # right
        if (face_r, face_c) == (0, 2):
            return (
                (face_size - 1 - local_r) + 2 * face_size,
                (face_size - 1) + 1 * face_size,
                2,
            )
        elif (face_r, face_c) == (1, 1):
            return (face_size - 1) + 0 * face_size, local_r + 2 * face_size, 3
        elif (face_r, face_c) == (2, 1):
            return (
                (face_size - 1 - local_r) + 0 * face_size,
                (face_size - 1) + 2 * face_size,
                2,
            )
        elif (face_r, face_c) == (3, 0):
            return (face_size - 1) + 2 * face_size, local_r + 1 * face_size, 3
        return row, col + 1, facing
    elif facing == 1:  # down
        if (face_r, face_c) == (0, 2):
            return local_c + 1 * face_size, (face_size - 1) + 1 * face_size, 2
        elif (face_r, face_c) == (2, 1):
            return local_c + 3 * face_size, (face_size - 1) + 0 * face_size, 2
        elif (face_r, face_c) == (3, 0):
            return 0 + 0 * face_size, local_c + 2 * face_size, 1
        return row + 1, col, facing
    elif facing == 2:  # left
        if (face_r, face_c) == (0, 1):
            return (face_size - 1 - local_r) + 2 * face_size, 0 + 0 * face_size, 0
        elif (face_r, face_c) == (1, 1):
            return 0 + 2 * face_size, local_r + 0 * face_size, 1
        elif (face_r, face_c) == (2, 0):
            return (face_size - 1 - local_r) + 0 * face_size, 0 + 1 * face_size, 0
        elif (face_r, face_c) == (3, 0):
            return 0 + 0 * face_size, local_r + 1 * face_size, 1
        return row, col - 1, facing
    else:  # up
        if (face_r, face_c) == (0, 1):
            return local_c + 3 * face_size, 0 + 0 * face_size, 0
        elif (face_r, face_c) == (0, 2):
            return (face_size - 1) + 3 * face_size, local_c + 0 * face_size, 3
        elif (face_r, face_c) == (2, 0):
            return local_c + 1 * face_size, 0 + 1 * face_size, 0
        return row - 1, col, facing


def part_one():
    grid, path = parse_input()
    start_col = min(c for r, c in grid if r == 0)
    row, col = 0, start_col
    facing = 0
    for instruction in path:
        if isinstance(instruction, int):
            dr, dc = DIRS[facing]
            for _ in range(instruction):
                nr = row + dr
                nc = col + dc
                if (nr, nc) not in grid:
                    nr, nc = wrap_2d(grid, row, col, dr, dc)
                if grid[(nr, nc)] == "#":
                    break
                row, col = nr, nc
        else:
            facing = turn(facing, instruction)
    return 1000 * (row + 1) + 4 * (col + 1) + facing


def part_two():
    grid, path = parse_input()
    _, _, face_size = get_cube_faces(grid)
    start_col = min(c for r, c in grid if r == 0)
    row, col = 0, start_col
    facing = 0

    for instruction in path:
        if isinstance(instruction, int):
            for _ in range(instruction):
                dr, dc = DIRS[facing]
                nr = row + dr
                nc = col + dc
                nfacing = facing
                if (nr, nc) not in grid:
                    nr, nc, nfacing = wrap_cube(row, col, facing, face_size)
                if grid[(nr, nc)] == "#":
                    break
                row, col, facing = nr, nc, nfacing
        else:
            facing = turn(facing, instruction)

    return 1000 * (row + 1) + 4 * (col + 1) + facing


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
