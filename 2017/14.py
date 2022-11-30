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
            self.state[a], self.state[b] = self.state[b], self.state[a]
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

    def calc_hash(self, s):
        lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
        for _ in range(64):
            self.twist_sequence(lengths)
        return self.knot_hash()


INPUT = "hxtvlmkl"


def part_one():
    return sum(
        bin(int(Knot(256).calc_hash(f"{INPUT}-{i}"), 16)).count("1")
        for i in range(128)
    )


def part_two():
    def flood_fill(i, j):
        if (
            i < 0
            or i >= len(grid)
            or j < 0
            or j >= len(grid[i])
            or grid[i][j] == "0"
            or (i, j) in seen
        ):
            return
        seen.add((i, j))
        flood_fill(i - 1, j)
        flood_fill(i + 1, j)
        flood_fill(i, j - 1)
        flood_fill(i, j + 1)

    grid = [
        bin(int(Knot(256).calc_hash(f"{INPUT}-{i}"), 16))[2:].zfill(128)
        for i in range(128)
    ]
    seen = set()
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1" and (i, j) not in seen:
                flood_fill(i, j)
                res += 1
    return res


print(f"Part 1: {part_one()}")  # 8214
print(f"Part 2: {part_two()}")  # 1093
