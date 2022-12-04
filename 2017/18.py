from collections import defaultdict, deque

with open("18.txt", "r") as file:
    data = file.read().strip()

INSTRUCTIONS = [line.split() for line in data.split("\n")]


class Duet:
    def __init__(self, instructions, part2=False, pid=0):
        self.instructions = instructions
        self.registers = defaultdict(int)
        self.registers["p"] = pid
        self.last_played = None
        self.i = 0
        self.part2 = part2
        self.pair = None
        self.queue = deque()
        self.send_count = 0

    def run(self):
        while self.i < len(self.instructions):
            instruction = self.instructions[self.i]
            if instruction[0] == "snd":
                if self.part2:
                    self.send(self.registers[instruction[1]])
                else:
                    self.last_played = self.registers[instruction[1]]
            elif instruction[0] == "set":
                self.registers[instruction[1]] = self.get_value(instruction[2])
            elif instruction[0] == "add":
                self.registers[instruction[1]] += self.get_value(instruction[2])
            elif instruction[0] == "mul":
                self.registers[instruction[1]] *= self.get_value(instruction[2])
            elif instruction[0] == "mod":
                self.registers[instruction[1]] %= self.get_value(instruction[2])
            elif instruction[0] == "rcv":
                if not self.part2:
                    if self.registers[instruction[1]] != 0:
                        return self.last_played
                if self.queue:
                    self.registers[instruction[1]] = self.queue.popleft()
                else:
                    return
            elif instruction[0] == "jgz":
                if self.get_value(instruction[1]) > 0:
                    self.i += self.get_value(instruction[2])
                    continue
            self.i += 1

    def get_value(self, value):
        try:
            return int(value)
        except ValueError:
            return self.registers[value]

    def send(self, value):
        self.pair.queue.append(value)
        self.send_count += 1


def part_one():
    duet = Duet(INSTRUCTIONS)
    return duet.run()


def part_two():
    duet0 = Duet(INSTRUCTIONS, part2=True, pid=0)
    duet1 = Duet(INSTRUCTIONS, part2=True, pid=1)
    duet0.pair = duet1
    duet1.pair = duet0
    while True:
        duet0.run()
        duet1.run()
        if not duet0.queue and not duet1.queue:
            return duet1.send_count


print(f"Part 1: {part_one()}")  # 2951
print(f"Part 2: {part_two()}")  # 7366
