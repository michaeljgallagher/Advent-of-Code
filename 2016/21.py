import re
from itertools import permutations


class Scrambler:
    def __init__(self, password, instructions):
        self.instructions = instructions
        self.password = list(password)

    def swap_pos(self, x, y):
        self.password[x], self.password[y] = self.password[y], self.password[x]

    def swap_letter(self, x, y):
        self.swap_pos(self.password.index(x), self.password.index(y))

    def rotate(self, direction, steps):
        if direction == "right":
            steps = -steps
        steps %= len(self.password)
        self.password = self.password[steps:] + self.password[:steps]

    def rotate_pos(self, x):
        i = self.password.index(x)
        steps = 1 + i + (i >= 4)
        self.rotate("right", steps)

    def reverse(self, x, y):
        self.password[x : y + 1] = self.password[x : y + 1][::-1]

    def move(self, x, y):
        self.password.insert(y, self.password.pop(x))

    def scramble(self):
        for instruction in self.instructions:
            getattr(self, instruction[0])(*instruction[1:])
        return "".join(self.password)


with open("21.txt", "r") as file:
    data = file.read().strip()


def parse_input(data):
    res = []
    for line in data.split("\n"):
        if m := re.search(r"swap position (\d+) .+ (\d+)", line):
            res.append(("swap_pos", int(m.group(1)), int(m.group(2))))
        elif m := re.search(r"swap letter (\w) .+ (\w)", line):
            res.append(("swap_letter", m.group(1), m.group(2)))
        elif m := re.search(r"rotate (left|right) (\d+)", line):
            res.append(("rotate", m.group(1), int(m.group(2))))
        elif m := re.search(r"rotate based on position of letter (\w)", line):
            res.append(("rotate_pos", m.group(1)))
        elif m := re.search(r"reverse .+ (\d+) .+ (\d+)", line):
            res.append(("reverse", int(m.group(1)), int(m.group(2))))
        elif m := re.search(r"move position (\d+) .+ (\d+)", line):
            res.append(("move", int(m.group(1)), int(m.group(2))))
    return res


INSTRUCTIONS = parse_input(data)


def part_one():
    return Scrambler("abcdefgh", INSTRUCTIONS).scramble()


def part_two():
    for p in permutations("fbgdceah"):
        if Scrambler(p, INSTRUCTIONS).scramble() == "fbgdceah":
            return "".join(p)


print(f"Part 1: {part_one()}")  # dgfaehcb
print(f"Part 2: {part_two()}")  # fdhgacbe
