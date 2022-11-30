class Dance:
    def __init__(self, programs):
        self.programs = programs

    def spin(self, n):
        self.programs = self.programs[-n:] + self.programs[:-n]

    def exchange(self, i, j):
        self.programs[i], self.programs[j] = self.programs[j], self.programs[i]

    def partner(self, a, b):
        i, j = self.programs.index(a), self.programs.index(b)
        self.exchange(i, j)

    def dance(self, moves):
        for move in moves:
            if move[0] == "s":
                self.spin(int(move[1:]))
            elif move[0] == "x":
                i, j = map(int, move[1:].split("/"))
                self.exchange(i, j)
            elif move[0] == "p":
                a, b = move[1:].split("/")
                self.partner(a, b)


with open("16.txt", "r") as file:
    data = file.read().strip()


def part_one(data):
    dance = Dance(list("abcdefghijklmnop"))
    dance.dance(data.split(","))
    return "".join(dance.programs)


def part_two(data):
    cur = "abcdefghijklmnop"
    dance = Dance(list(cur))
    seen = set()
    while cur not in seen:
        seen.add(cur)
        dance.dance(data.split(","))
        cur = "".join(dance.programs)
    dance = Dance(list("abcdefghijklmnop"))
    for _ in range(1000000000 % len(seen)):
        dance.dance(data.split(","))
    return "".join(dance.programs)


print(f"Part 1: {part_one(data)}")  # olgejankfhbmpidc
print(f"Part 2: {part_two(data)}")  # gfabehpdojkcimnl
