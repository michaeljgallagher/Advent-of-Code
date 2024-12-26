def parse_input():
    with open("23.txt", "r") as file:
        data = file.read()
    return [line.split() for line in data.splitlines()]


INSTRUCTIONS = parse_input()


class CPU:
    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = [0] * 8
        self.ops = {
            "set": self.set,
            "sub": self.sub,
            "mul": self.mul,
            "jnz": self.jnz,
        }
        self.idx = 0
        self.mul_count = 0

    def _get_val(self, x):
        return int(x) if x.lstrip("-").isdigit() else self.registers[ord(x) - ord("a")]

    def set(self, x, y):
        self.registers[ord(x) - ord("a")] = self._get_val(y)

    def sub(self, x, y):
        self.registers[ord(x) - ord("a")] -= self._get_val(y)

    def mul(self, x, y):
        self.mul_count += 1
        self.registers[ord(x) - ord("a")] *= self._get_val(y)

    def jnz(self, x, y):
        if self._get_val(x) != 0:
            self.idx += self._get_val(y)

    def step(self):
        op, x, y = self.instructions[self.idx]
        self.ops[op](x, y)
        if op != "jnz" or self._get_val(x) == 0:
            self.idx += 1

    def run(self):
        while 0 <= self.idx < len(self.instructions):
            self.step()
        return self.mul_count


def prime(n):
    if n == 2:
        return True
    if n & 1 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def part_one():
    return CPU(INSTRUCTIONS).run()


def part_two():
    cpu = CPU(INSTRUCTIONS)
    cpu.registers[0] = 1
    for _ in range(7):
        cpu.step()
    b, c = cpu.registers[1:3]
    return sum(not prime(i) for i in range(b, c + 1, 17))


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
