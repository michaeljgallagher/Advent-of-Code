from intcode import Intcode


def parse_input():
    with open("19.txt") as data:
        program = list(map(int, data.read().split(",")))
    return program


PROGRAM = parse_input()


def check_beam(program, i, j):
    comp = Intcode(program[:])
    res = comp.run_until_halt([i, j])
    return res[0] if res else 0


def find_beam_edges(program, j, start_i=0):
    left = None
    right = None

    # find left edge
    i = start_i
    while i < j * 2 + 10:  # reasonable bound
        if check_beam(program, i, j):
            left = i
            break
        i += 1
    if left is None:
        return None, None

    # find right edge
    i = left
    while check_beam(program, i, j):
        right = i
        i += 1
    return left, right


def part_one():
    res = 0
    for i in range(50):
        for j in range(50):
            res += check_beam(PROGRAM, i, j)
    return res


def part_two():
    j = 100  # start at 100
    prev_left = 0
    while True:
        left, right = find_beam_edges(PROGRAM, j, prev_left)
        if left is None:
            j += 1
            continue
        prev_left = left
        width = right - left + 1
        if width >= 100:
            top_j = j - 99
            right_i = left + 99
            if top_j >= 0 and check_beam(PROGRAM, right_i, top_j):
                return left * 10000 + top_j
        j += 1


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
