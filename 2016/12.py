import re

with open("12.txt", "r") as file:
    data = file.read().strip()

INSTRUCTIONS = [re.split(r"[ ,]+", line.strip()) for line in data.split("\n")]


class CPU:
    def __init__(self, instructions, reg_c=0):
        self.registers = {"a": 0, "b": 0, "c": reg_c, "d": 0}
        self.pos = 0
        self.instructions = instructions

    def cpy(self, x, y):
        if x in self.registers:
            self.registers[y] = self.registers[x]
        else:
            self.registers[y] = int(x)
        self.pos += 1

    def inc(self, x):
        self.registers[x] += 1
        self.pos += 1

    def dec(self, x):
        self.registers[x] -= 1
        self.pos += 1

    def jnz(self, x, y):
        if self.registers.get(x, 1) != 0:
            self.pos += int(y)
        else:
            self.pos += 1

    def step(self):
        op, *args = self.instructions[self.pos]
        getattr(self, op)(*args)

    def run(self):
        while 0 <= self.pos < len(self.instructions):
            self.step()
        return self.registers["a"]


def part_one():
    cpu = CPU(INSTRUCTIONS)
    return cpu.run()


def part_two():
    cpu = CPU(INSTRUCTIONS, 1)
    return cpu.run()


print(f"Part 1: {part_one()}")  # 317993
print(f"Part 2: {part_two()}")  # 9227647
