import re
from itertools import count

with open("25.txt", "r") as file:
    data = file.read().strip()


class CPU:
    def __init__(self, instructions, reg_a=0):
        self.registers = {"a": reg_a, "b": 0, "c": 0, "d": 0}
        self.pos = 0
        self.instructions = instructions
        self.transmission = []

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
        if x in self.registers:
            if self.registers[x] != 0:
                self.pos += (
                    int(y)
                    if y.lstrip("-").isdigit()
                    else self.registers.get(y, 1)
                )
            else:
                self.pos += 1
        elif int(x) != 0:
            self.pos += (
                int(y) if y.lstrip("-").isdigit() else self.registers.get(y, 1)
            )
        else:
            self.pos += 1

    def out(self, x):
        self.transmission.append(self.registers[x])
        self.pos += 1

    def step(self):
        op, *args = self.instructions[self.pos]
        getattr(self, op)(*args)

    def run(self):
        while len(self.transmission) < 20:
            self.step()
        return self.transmission == [0, 1] * 10


def part_one():
    for i in count():
        insts = [re.split(r"[ ,]+", line.strip()) for line in data.split("\n")]
        cpu = CPU(insts, reg_a=i)
        if cpu.run():
            return i


print(f"Part 1: {part_one()}")  # 180
