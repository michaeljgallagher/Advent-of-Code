def parse_input():
    with open("21.txt", "r") as file:
        lines = file.read().strip().splitlines()
    ip_reg = int(lines[0].split()[1])
    program = []
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = line.split()
        op = parts[0]
        a, b, c = map(int, parts[1:])
        program.append((op, a, b, c))
    return ip_reg, program


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


def part_one():
    ip_reg, program = parse_input()
    reg = [0] * 6
    ip = 0
    while 0 <= ip < len(program):
        if ip == 28:
            return reg[4]
        reg[ip_reg] = ip
        op, a, b, c = program[ip]
        OPS[op](reg, a, b, c)
        ip = reg[ip_reg]
        ip += 1
    return None


def part_two():
    ip_reg, program = parse_input()
    reg = [0] * 6
    ip = 0
    seen = set()
    prev = None
    while 0 <= ip < len(program):
        if ip == 28:
            value = reg[4]
            if value in seen:
                return prev
            seen.add(value)
            prev = value
        if ip == 17:
            reg[2] = reg[3] >> 8
            reg[3] = reg[2]
            ip = 8
            reg[ip_reg] = ip
            continue
        reg[ip_reg] = ip
        op, a, b, c = program[ip]
        OPS[op](reg, a, b, c)
        ip = reg[ip_reg]
        ip += 1


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
