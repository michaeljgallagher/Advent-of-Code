from collections import Counter
from itertools import chain

with open("07.txt", "r") as file:
    data = file.read().strip()

HANDS = [(a, int(b)) for x in data.split("\n") for a, b in [x.split(" ")]]
HAND_TYPES = [
    lambda x, j: len(x) < 2,
    lambda x, j: max(x.values()) + j == 4,
    lambda x, j: (len(x) == 2 and 2 in x.values() and 3 in x.values())
    or (Counter(x.values())[2] == 2 and j == 1),
    lambda x, j: (3 - j) in x.values(),
    lambda x, j: (2 in Counter(x.values()) and Counter(x.values())[2] == 2)
    or (j > 0 and 2 in Counter(x.values())),
    lambda x, j: (2 - j) in x.values(),
]


def solve(part_two=False):
    sorted_hands = [[] for _ in range(7)]
    order = {
        v: i for i, v in enumerate("J23456789TQKA" if part_two else "23456789TJQKA")
    }

    for hand, bid in HANDS:
        cur = Counter(hand)
        if part_two:
            jokers = cur["J"]
            del cur["J"]
        else:
            jokers = 0
        i = next(
            (i for i, hand_type in enumerate(HAND_TYPES) if hand_type(cur, jokers)), 6
        )
        sorted_hands[i].append((hand, bid))

    for i, v in enumerate(sorted_hands):
        sorted_hands[i] = sorted(v, key=lambda x: [order[c] for c in x[0]])

    return sum(
        i * bid
        for i, (hand, bid) in enumerate(
            chain.from_iterable(sorted_hands[::-1]), start=1
        )
    )


print(f"Part 1: {solve()}")  # 253866470
print(f"Part 2: {solve(True)}")  # 254494947
