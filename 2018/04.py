import re
from collections import Counter, defaultdict


def parse_input():
    with open("04.txt", "r") as file:
        data = file.read()
    data = re.findall(r"\[(\d{4})-(\d\d)-(\d\d) (\d\d):(\d\d)\] (.+)", data)
    data = sorted(tuple(map(int, x[:5])) + (x[5],) for x in data)
    guards = defaultdict(Counter)
    for _, _, _, _, minute, record in data:
        if record.startswith("Guard"):
            cur = int(re.search(r"\d+", record).group())
        elif record.startswith("falls"):
            s = minute
        else:
            for t in range(s, minute):
                guards[cur][t] += 1
    return guards


GUARDS = parse_input()


def part_one():
    guard, minutes = max(GUARDS.items(), key=lambda x: sum(x[1].values()))
    return guard * minutes.most_common(1)[0][0]


def part_two():
    guard, minutes = max(GUARDS.items(), key=lambda x: x[1].most_common(1)[0][1])
    return guard * minutes.most_common(1)[0][0]


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
