import re


class CPU:
    def __init__(self, instructions, part_two=False):
        self.instructions = instructions
        self.pos = 0
        self.x = 1
        self.cycles = 0
        self.strength = 0
        self.part_two = part_two
        self.grid = [[" " for _ in range(40)] for _ in range(6)]

    def addx(self, y):
        self.cycle()
        self.cycle()
        self.x += int(y)

    def noop(self):
        self.cycle()

    def cycle(self):
        self.cycles += 1
        if self.part_two:
            self.check_two()
        else:
            self.check()

    def check(self):
        if self.cycles % 40 == 20:
            self.strength += self.x * self.cycles

    def check_two(self):
        if self.x - 1 <= (self.cycles - 1) % 40 <= self.x + 1:
            self.grid[self.cycles // 40][(self.cycles - 1) % 40] = "#"

    def step(self):
        op, *args = self.instructions[self.pos]
        getattr(self, op)(*args)
        self.pos += 1

    def run(self):
        while 0 <= self.pos < len(self.instructions):
            self.step()


with open("10.txt", "r") as file:
    data = file.read().strip()

INSTRUCTIONS = [re.split(r"[ ,]+", line.strip()) for line in data.split("\n")]


def part_one():
    cpu = CPU(INSTRUCTIONS)
    cpu.run()
    return cpu.strength


def part_two():
    cpu = CPU(INSTRUCTIONS, part_two=True)
    cpu.run()
    print("\n".join("".join(row) for row in cpu.grid))


print(f"Part 1: {part_one()}")  # 11720
print(f"Part 2: {part_two()}")  # ERCREPCJ
