from itertools import count

with open("06.txt", "r") as file:
    data = file.read().strip()

BANKS = [int(x) for x in data.split()]


def reallocate(banks):
    banks = banks[:]
    i = banks.index(max(banks))
    blocks = banks[i]
    banks[i] = 0
    while blocks:
        i = (i + 1) % len(banks)
        banks[i] += 1
        blocks -= 1
    return banks


def run_cycle(banks):
    seen = {}
    for i in count():
        if tuple(banks) not in seen:
            seen[tuple(banks)] = i
            banks = reallocate(banks)
        else:
            return len(seen), i - seen[tuple(banks)]


part_one, part_two = run_cycle(BANKS)

print(f"Part 1: {part_one}")  # 11137
print(f"Part 2: {part_two}")  # 1037
