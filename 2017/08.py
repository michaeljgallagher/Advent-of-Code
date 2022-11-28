import re
from collections import defaultdict
from operator import eq, ge, gt, le, lt, ne


class CPU:
    def __init__(self, instructions):
        self.registers = defaultdict(int)
        self.instructions = instructions
        self.ops = {
            "<": lt,
            "<=": le,
            "==": eq,
            "!=": ne,
            ">=": ge,
            ">": gt,
        }
        self.max_mem = 0

    def inc(self, x, y):
        self.registers[x] += y

    def dec(self, x, y):
        self.registers[x] -= y

    def eval_condition(self, x, op, y):
        return self.ops[op](self.registers[x], y)

    def step(self, *args):
        op, reg_a, x, reg_b, cond, y = args
        if self.eval_condition(reg_b, cond, y):
            getattr(self, op)(reg_a, x)
            self.max_mem = max(self.max_mem, self.registers[reg_a])

    def run(self, part_two=False):
        for line in self.instructions:
            self.step(*line)
        return self.max_mem if part_two else max(self.registers.values())


with open("08.txt", "r") as file:
    data = file.read().strip()

INSTRUCTIONS = [
    (op, reg_a, int(x), reg_b, cond, int(y))
    for reg_a, op, x, reg_b, cond, y in re.findall(
        r"(\w+) (inc|dec) (-?\d+) if (\w+) ([<>=!]+) (-?\d+)", data
    )
]

print(f"Part 1: {CPU(INSTRUCTIONS).run()}")  # 5752
print(f"Part 2: {CPU(INSTRUCTIONS).run(part_two=True)}")  # 6366
