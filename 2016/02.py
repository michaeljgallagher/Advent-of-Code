with open("02.txt", "r") as file:
    data = file.read().strip()

INSTRUCTIONS = data.split("\n")
KEYPAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
KEYPAD2 = [
    [".", ".", "1", ".", "."],
    [".", "2", "3", "4", "."],
    ["5", "6", "7", "8", "9"],
    [".", "A", "B", "C", "."],
    [".", ".", "D", ".", "."],
]
DIRS = {
    "U": 0 - 1j,
    "D": 0 + 1j,
    "L": -1 + 0j,
    "R": 1 + 0j,
}


def find_key(moves, keypad, pos):
    N, M = len(keypad), len(keypad[0])
    for c in moves:
        npos = pos + DIRS[c]
        ni, nj = int(npos.imag), int(npos.real)
        if 0 <= ni < N and 0 <= nj < M and keypad[ni][nj] != ".":
            pos = npos
    i, j = int(pos.imag), int(pos.real)
    return keypad[i][j], pos


def part_one():
    res, pos = 0, 1 + 1j
    for moves in INSTRUCTIONS:
        key, npos = find_key(moves, KEYPAD, pos)
        res = res * 10 + key
        pos = npos
    return res


def part_two():
    res, pos = [], 2j
    for moves in INSTRUCTIONS:
        key, npos = find_key(moves, KEYPAD2, pos)
        res.append(key)
        pos = npos
    return "".join(res)


print(f"Part 1: {part_one()}")  # 56983
print(f"Part 2: {part_two()}")  # 8B8B1
