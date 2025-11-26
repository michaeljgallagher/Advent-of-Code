from collections import deque

from intcode import Intcode


def parse_input():
    with open("23.txt", "r") as file:
        data = file.read()
    return list(map(int, data.split(",")))


def solve(pt2=False):
    program = parse_input()
    computers = [Intcode(program) for _ in range(50)]
    for i, computer in enumerate(computers):
        computer.add_input(i)
    packets = [deque() for _ in range(50)]
    nat_packet = None
    prev_nat_y = None
    while True:
        idle = True
        for i, computer in enumerate(computers):
            if packets[i]:
                x, y = packets[i].popleft()
                computer.add_input(x)
                computer.add_input(y)
                idle = False
            else:
                computer.add_input(-1)
            computer.run(pause_on_output=False)
            while len(computer.output_queue) >= 3:
                dest = computer.get_output()
                x = computer.get_output()
                y = computer.get_output()
                idle = False
                if dest == 255:
                    if not pt2:
                        return y
                    nat_packet = (x, y)
                elif 0 <= dest < 50:
                    packets[dest].append((x, y))
        if idle and nat_packet:
            x, y = nat_packet
            if y == prev_nat_y:
                return y
            prev_nat_y = y
            packets[0].append((x, y))


print(f"Part 1: {solve()}")
print(f"Part 2: {solve(pt2=True)}")
