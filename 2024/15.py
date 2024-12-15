def parse_input():
    with open("15.txt", "r") as file:
        data = file.read()
    grid_raw, moves_raw = data.split("\n\n")
    grid = [list(row) for row in grid_raw.splitlines()]
    moves = moves_raw.replace("\n", "")
    grid_2_raw = (
        grid_raw.replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
    )
    grid_2 = [list(row) for row in grid_2_raw.splitlines()]
    return grid, grid_2, moves


GRID_1, GRID_2, MOVES = parse_input()
DIRS = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}


def possible(i, j, di):
    ni = i + di
    adjacent = 1 if GRID_2[i][j] == "[" else -1
    if GRID_2[ni][j] == "#" or GRID_2[ni][j + adjacent] == "#":
        return False
    if GRID_2[ni][j] in "[]" and not possible(ni, j, di):
        return False
    if GRID_2[ni][j + adjacent] in "[]" and not possible(ni, j + adjacent, di):
        return False
    return True


def move(i, j, di):
    ni = i + di
    adjacent = 1 if GRID_2[i][j] == "[" else -1
    if GRID_2[ni][j] in "[]":
        move(ni, j, di)
    if GRID_2[ni][j + adjacent] in "[]":
        move(ni, j + adjacent, di)
    GRID_2[i][j], GRID_2[ni][j] = GRID_2[ni][j], GRID_2[i][j]
    GRID_2[i][j + adjacent], GRID_2[ni][j + adjacent] = (
        GRID_2[ni][j + adjacent],
        GRID_2[i][j + adjacent],
    )


def part_one():
    i, j = next(
        (i, j) for i, row in enumerate(GRID_1) for j, v in enumerate(row) if v == "@"
    )
    GRID_1[i][j] = "."
    for c in MOVES:
        di, dj = DIRS[c]
        ni, nj = i + di, j + dj
        if GRID_1[ni][nj] == "#":
            continue
        if GRID_1[ni][nj] == ".":
            i, j = ni, nj
        if GRID_1[ni][nj] == "O":
            nni, nnj = ni, nj
            while GRID_1[nni][nnj] == "O":
                nni += di
                nnj += dj
            if GRID_1[nni][nnj] == "#":
                continue
            GRID_1[ni][nj], GRID_1[nni][nnj] = GRID_1[nni][nnj], GRID_1[ni][nj]
            i, j = ni, nj
    return sum(
        i * 100 + j
        for i, row in enumerate(GRID_1)
        for j, v in enumerate(row)
        if v == "O"
    )


def part_two():
    i, j = next(
        (i, j) for i, row in enumerate(GRID_2) for j, v in enumerate(row) if v == "@"
    )
    GRID_2[i][j] = "."
    for c in MOVES:
        di, dj = DIRS[c]
        ni, nj = i + di, j + dj
        if GRID_2[ni][nj] == "#":
            continue
        elif GRID_2[ni][nj] == ".":
            i, j = ni, nj
        elif GRID_2[ni][nj] in "[]":
            if di and possible(ni, nj, di):
                move(ni, nj, di)
                i, j = ni, nj
            elif dj:
                nnj = nj
                while GRID_2[ni][nnj] in "[]":
                    nnj += dj
                if GRID_2[ni][nnj] == "#":
                    continue
                while nnj != nj:
                    GRID_2[ni][nnj] = GRID_2[ni][nnj - dj]
                    nnj -= dj
                GRID_2[ni][nj] = "."
                i, j = ni, nj
    return sum(
        i * 100 + j
        for i, row in enumerate(GRID_2)
        for j, v in enumerate(row)
        if v == "["
    )


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
