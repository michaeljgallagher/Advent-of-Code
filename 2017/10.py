from functools import reduce


class Knot:
    def __init__(self, size):
        self.size = size
        self.state = list(range(size))
        self.pos = 0
        self.skip = 0

    def twist(self, length):
        for i in range(length >> 1):
            a = (self.pos + i) % self.size
            b = (self.pos + length - 1 - i) % self.size
            self.state[a], self.state[b] = (
                self.state[b],
                self.state[a],
            )
        self.pos = (self.pos + length + self.skip) % self.size
        self.skip += 1

    def twist_sequence(self, lengths):
        for length in lengths:
            self.twist(length)

    def dense_hash(self):
        return [
            reduce(lambda a, b: a ^ b, self.state[i : i + 16])
            for i in range(0, self.size, 16)
        ]

    def knot_hash(self):
        return "".join(f"{x:02x}" for x in self.dense_hash())


with open("10.txt", "r") as file:
    data = file.read().strip()


def part_one(data):
    lengths = list(map(int, data.split(",")))
    knot = Knot(256)
    knot.twist_sequence(lengths)
    return knot.state[0] * knot.state[1]


def part_two(data):
    lengths = [ord(c) for c in data] + [17, 31, 73, 47, 23]
    knot = Knot(256)
    for _ in range(64):
        knot.twist_sequence(lengths)
    return knot.knot_hash()


print(f"Part 1: {part_one(data)}")  # 6909
print(f"Part 2: {part_two(data)}")  # 9d5f4561367d379cfbf04f8c471c0095
