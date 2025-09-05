import re
from collections import defaultdict
from copy import deepcopy


def parse_input():
    with open("16.txt", "r") as file:
        data = file.read()
    lines = data.strip().splitlines()
    samples = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("Before"):
            before = list(map(int, re.findall(r"\d+", lines[i])))
            instr = list(map(int, lines[i + 1].split()))
            after = list(map(int, re.findall(r"\d+", lines[i + 2])))
            samples.append((before, instr, after))
            i += 4
        else:
            break
    program = [list(map(int, line.split())) for line in lines[i:] if line.strip()]
    return samples, program


SAMPLES, PROGRAM = parse_input()


def addr(reg, a, b, c):
    reg[c] = reg[a] + reg[b]


def addi(reg, a, b, c):
    reg[c] = reg[a] + b


def mulr(reg, a, b, c):
    reg[c] = reg[a] * reg[b]


def muli(reg, a, b, c):
    reg[c] = reg[a] * b


def banr(reg, a, b, c):
    reg[c] = reg[a] & reg[b]


def bani(reg, a, b, c):
    reg[c] = reg[a] & b


def borr(reg, a, b, c):
    reg[c] = reg[a] | reg[b]


def bori(reg, a, b, c):
    reg[c] = reg[a] | b


def setr(reg, a, b, c):
    reg[c] = reg[a]


def seti(reg, a, b, c):
    reg[c] = a


def gtir(reg, a, b, c):
    reg[c] = int(a > reg[b])


def gtri(reg, a, b, c):
    reg[c] = int(reg[a] > b)


def gtrr(reg, a, b, c):
    reg[c] = int(reg[a] > reg[b])


def eqir(reg, a, b, c):
    reg[c] = int(a == reg[b])


def eqri(reg, a, b, c):
    reg[c] = int(reg[a] == b)


def eqrr(reg, a, b, c):
    reg[c] = int(reg[a] == reg[b])


OPS = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr,
}


def match_ops(before, instr, after):
    _, a, b, c = instr
    res = set()
    for name, f in OPS.items():
        regs = deepcopy(before)
        f(regs, a, b, c)
        if regs == after:
            res.add(name)
    return res


def run(program, mapping):
    reg = [0] * 4
    for op, a, b, c in program:
        OPS[mapping[op]](reg, a, b, c)
    return reg


def part_one():
    return sum(len(match_ops(*sample)) >= 3 for sample in SAMPLES)


def part_two():
    possible = defaultdict(lambda: set(OPS.keys()))
    for before, instr, after in SAMPLES:
        op, _, _, _ = instr
        matches = match_ops(before, instr, after)
        possible[op] &= matches
    mapping = {}
    while possible:
        found = list(filter(lambda x: len(x[1]) == 1, possible.items()))
        for op, s in found:
            f = s.pop()
            mapping[op] = f
            del possible[op]
            for fs in possible.values():
                fs.discard(f)
    reg = run(PROGRAM, mapping)
    return reg[0]


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
