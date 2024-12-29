from itertools import count


def parse_input():
    with open("12.txt", "r") as file:
        data = file.read()
    state, notes = data.split("\n\n")
    state = state.split()[-1]
    notes = {k: v for line in notes.splitlines() for k, v in [line.split(" => ")]}
    return state, notes


def step(state, notes, left):
    state = "....." + state + ".."
    n = len(state)
    nstate = []
    for i in range(n):
        cur = state[i - 2 : i + 3]
        nstate.append(notes.get(cur, "."))
    state = "".join(nstate)
    left += 5
    res = sum(i for i, v in enumerate(state, start=-left) if v == "#")
    return state, left, res


def part_one():
    state, notes = parse_input()
    left = 0
    for _ in range(20):
        state, left, res = step(state, notes, left)
    return res


def part_two():
    state, notes = parse_input()
    left = 0
    prev = 0
    diff = 0
    for t in count():
        state, left, cur = step(state, notes, left)
        if diff == cur - prev:
            return diff * (50_000_000_000 - t) + prev
        diff = cur - prev
        prev = cur


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
