import re

with open("23.txt", "r") as file:
    data = file.read().strip()

INSTRUCTIONS = [re.split(r"[ ,]+", line.strip()) for line in data.split("\n")]


class CPU:
    def __init__(self, instructions, reg_a=0):
        self.registers = {"a": reg_a, "b": 0}
        self.pos = 0
        self.instructions = instructions

    def hlf(self, r):
        self.registers[r] >>= 1
        self.pos += 1

    def tpl(self, r):
        self.registers[r] *= 3
        self.pos += 1

    def inc(self, r):
        self.registers[r] += 1
        self.pos += 1

    def jmp(self, offset):
        self.pos += int(offset)

    def jie(self, r, offset):
        self.pos += int(offset) if not self.registers[r] & 1 else 1

    def jio(self, r, offset):
        self.pos += int(offset) if self.registers[r] == 1 else 1

    def step(self):
        op, *args = self.instructions[self.pos]
        getattr(self, op)(*args)

    def run(self):
        while 0 <= self.pos < len(self.instructions):
            self.step()
        return self.registers["b"]


def part_one():
    cpu = CPU(INSTRUCTIONS)
    return cpu.run()


def part_two():
    cpu = CPU(INSTRUCTIONS, 1)
    return cpu.run()


print(f"Part 1: {part_one()}")  # 307
print(f"Part 2: {part_two()}")  # 160
