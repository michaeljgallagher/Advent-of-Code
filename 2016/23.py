import re

with open("23.txt", "r") as file:
    data = file.read().strip()


class CPU:
    def __init__(self, instructions, reg_a=0, pt2=False):
        self.registers = {"a": reg_a, "b": 0, "c": 0, "d": 0}
        self.pos = 0
        self.instructions = instructions
        self.pt2 = pt2

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

    def tgl(self, x):
        if x in self.registers:
            x = self.registers[x]
        else:
            x = int(x)
        if 0 <= self.pos + x < len(self.instructions):
            op, *args = self.instructions[self.pos + x]
            if len(args) == 1:
                if op == "inc":
                    self.instructions[self.pos + x][0] = "dec"
                else:
                    self.instructions[self.pos + x][0] = "inc"
            else:
                if op == "jnz":
                    self.instructions[self.pos + x][0] = "cpy"
                else:
                    self.instructions[self.pos + x][0] = "jnz"
        self.pos += 1

    def mul(self, x, y, z):
        if x in self.registers:
            self.registers[z] += self.registers[x] * self.registers[y]
        else:
            self.registers[z] += int(x) * self.registers[y]
        self.pos += 1

    def step(self):
        op, *args = self.instructions[self.pos]
        getattr(self, op)(*args)

    def run(self):
        if self.pt2:
            self.instructions[4] = ["mul", "b", "d", "a"]
            self.instructions[5:10] = [["jnz", "0", "0"] for _ in range(5)]
        while 0 <= self.pos < len(self.instructions):
            self.step()
        return self.registers["a"]


def part_one():
    instructions = [
        re.split(r"[ ,]+", line.strip()) for line in data.split("\n")
    ]
    cpu = CPU(instructions, 7)
    return cpu.run()


def part_two():
    instructions = [
        re.split(r"[ ,]+", line.strip()) for line in data.split("\n")
    ]
    cpu = CPU(instructions, 12, True)
    return cpu.run()


print(f"Part 1: {part_one()}")  # 11514
print(f"Part 2: {part_two()}")  # 479008074
