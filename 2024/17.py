import re


def parse_input():
    with open("17.txt", "r") as file:
        data = file.read()
    nums = list(map(int, re.findall(r"(\d+)", data)))
    a, b, c = nums[:3]
    program = nums[3:]
    return a, b, c, program


A, B, C, PROGRAM = parse_input()


class OpCode:
    def __init__(self, a, b, c, program):
        self.program = program
        self.a = a
        self.b = b
        self.c = c
        self.ops = [
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv,
        ]
        self.idx = 0
        self.output = []

    def _combo(self, val):
        return [0, 1, 2, 3, self.a, self.b, self.c][val]

    def adv(self, val):
        x = self._combo(val)
        self.a = int(self.a / (1 << x))

    def bxl(self, val):
        self.b ^= val

    def bst(self, val):
        x = self._combo(val)
        self.b = x % 8

    def jnz(self, val):
        if self.a == 0:
            return
        self.idx = val - 2

    def bxc(self, val):
        self.b ^= self.c

    def out(self, val):
        x = self._combo(val) % 8
        self.output.append(x)

    def bdv(self, val):
        x = self._combo(val)
        self.b = int(self.a / (1 << x))

    def cdv(self, val):
        x = self._combo(val)
        self.c = int(self.a / (1 << x))

    def step(self):
        op, val = self.program[self.idx], self.program[self.idx + 1]
        self.ops[op](val)

    def run(self):
        while self.idx < len(self.program):
            self.step()
            self.idx += 2
        return self.output


def dfs(i, cur):
    for x in range(8):
        if OpCode(cur * 8 + x, 0, 0, PROGRAM).run() == PROGRAM[i:]:
            if i == 0:
                return cur * 8 + x
            res = dfs(i - 1, cur * 8 + x)
            if res:
                return res
    return


def part_one():
    return ",".join(map(str, OpCode(A, B, C, PROGRAM).run()))


def part_two():
    return dfs(len(PROGRAM) - 1, 0)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
