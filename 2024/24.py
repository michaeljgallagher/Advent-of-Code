import operator
import re


def parse_input():
    with open("24.txt", "r") as file:
        data = file.read()
    wires, gates = data.split("\n\n")
    wires = re.findall(r"(\w\d\d): (0|1)", wires)
    wires = {k: int(v) for k, v in wires}
    gates = re.findall(r"([\w\d]{3}) (AND|OR|XOR) ([\w\d]{3}) -> ([\w\d]{3})", gates)
    gates = {k: (a, b, c) for a, b, c, k in gates}
    return wires, gates


WIRES, GATES = parse_input()
OPS = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}


def part_one():
    def evaluate(gate):
        a, op, b = gate
        for wire in (a, b):
            if wire not in WIRES:
                WIRES[wire] = evaluate(GATES[wire])
        return OPS[op](WIRES[a], WIRES[b])

    return int(
        "".join(
            str(evaluate(GATES[z]))
            for z in sorted(GATES.keys(), reverse=True)
            if z.startswith("z")
        ),
        2,
    )


def part_two():
    return ",".join(
        sorted(
            c
            for c, (a, op, b) in GATES.items()
            if (
                (c.startswith("z") and op != "XOR" and c != "z45")
                or (
                    op == "XOR"
                    and all(not x.startswith(("x", "y", "z")) for x in (a, b, c))
                )
                or (
                    op == "AND"
                    and "x00" not in (a, b)
                    and any(
                        c in (aa, bb) and op2 != "OR"
                        for (aa, op2, bb) in GATES.values()
                    )
                )
                or (
                    op == "XOR"
                    and any(
                        c in (aa, bb) and op2 == "OR"
                        for (aa, op2, bb) in GATES.values()
                    )
                )
            )
        )
    )


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
