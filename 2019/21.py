from intcode import Intcode


def parse_input():
    with open("21.txt", "r") as file:
        data = file.read()
    return list(map(int, data.split(",")))


def solve(pt2=False):
    program = parse_input()
    computer = Intcode(program)
    springscript = [
        "NOT A J",  # J = !A
        "NOT B T",  # T = !B
        "OR T J",  # J = !A OR !B
        "NOT C T",  # T = !C
        "OR T J",  # J = !A OR !B OR !C
        "AND D J",  # J = (!A OR !B OR !C) AND D
    ]
    if pt2:
        springscript += [
            "NOT E T",  # T = !E
            "NOT T T",  # T = E (double negation to copy E to T)
            "OR H T",  # T = E OR H (can either step or jump after landing)
            "AND T J",  # J = (!A OR !B OR !C) AND D AND (E OR H)
        ]
    springscript.append("RUN" if pt2 else "WALK")
    inputs = [ord(c) for line in springscript for c in line + "\n"]
    return computer.run(inputs=inputs)[-1]


print(f"Part 1: {solve()}")
print(f"Part 2: {solve(pt2=True)}")
