import re


def parse_input():
    with open("25.txt", "r") as file:
        data = file.read()
    prelude, *bp = data.split("\n\n")
    state = prelude.splitlines()[0][-2]
    steps = int(re.search(r"(\d+)", prelude).group(1))
    regex = (
        r"In state (\w):\s+If the current value is 0:\s+- Write the value (\d).\s+"
        r"- Move one slot to the (\w+).\s+- Continue with state (\w).\s+"
        r"If the current value is 1:\s+- Write the value (\d).\s+"
        r"- Move one slot to the (\w+).\s+- Continue with state (\w)."
    )
    bp = [re.search(regex, section).groups() for section in bp]
    bp = {
        a: [
            (int(b), 1 if c == "right" else -1, d),
            (int(e), 1 if f == "right" else -1, g),
        ]
        for a, b, c, d, e, f, g in bp
    }
    return state, steps, bp


def part_one():
    state, steps, bp = parse_input()
    cur = 0
    seen = set()
    for _ in range(steps):
        write, direction, nstate = bp[state][int(cur in seen)]
        if write:
            seen.add(cur)
        else:
            seen.discard(cur)
        cur += direction
        state = nstate
    return len(seen)


print(f"Part 1: {part_one()}")
