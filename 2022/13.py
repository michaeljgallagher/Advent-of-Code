from ast import literal_eval
from math import prod

with open("13.txt", "r") as file:
    data = file.read().strip()


def parse_input(data):
    res = []
    for pair in data.split("\n\n"):
        a, b = pair.split("\n")
        res.append([literal_eval(a), literal_eval(b)])
    return res

PACKETS = parse_input(data)


class Packet:
    def __init__(self, packet):
        self.packet = packet

    def __lt__(self, other):
        return is_sorted(self.packet, other.packet)

    def __eq__(self, other):
        return self.packet == other.packet


def is_sorted(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return None if a == b else a < b
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]
    for x, y in zip(a, b):
        if (cur := is_sorted(x, y)) is not None:
            return cur
    return None if len(a) == len(b) else len(a) < len(b)


def part_one():
    return sum(
        i
        for i, (a, b) in enumerate(PACKETS, start=1)
        if is_sorted(a, b)
    )


def part_two():
    dividers = [Packet([[2]]), Packet([[6]])]
    packets = [
        Packet(packet) for pair in PACKETS for packet in pair
    ] + dividers
    packets.sort()
    return prod(map(lambda x: packets.index(x) + 1, dividers))


print(f"Part 1: {part_one()}")  # 5390
print(f"Part 2: {part_two()}")  # 19261
