import re
from itertools import combinations, product

with open("21.txt", "r") as file:
    data = file.read().strip()

WEAPONS = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]

ARMOR = [
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
    (0, 0, 0),
]

RINGS = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
    (0, 0, 0),
    (0, 0, 0),
]

BOSS_HP, BOSS_DAMAGE, BOSS_ARMOR = map(int, re.findall(r"(\d+)", data))


def attack(weapon_dmg, rings, boss_armor):
    return max(1, weapon_dmg + sum(rings) - boss_armor)


def defend(armor, rings, boss_dmg):
    return max(1, boss_dmg - armor - sum(rings))


def part_one():
    return min(
        weapon[0] + armor[0] + sum(r[0] for r in rings)
        for weapon, armor, rings in product(WEAPONS, ARMOR, combinations(RINGS, 2))
        if (BOSS_HP // attack(weapon[1], (r[1] for r in rings), BOSS_ARMOR))
        <= (100 // defend(armor[2], (r[2] for r in rings), BOSS_DAMAGE))
    )


def part_two():
    return max(
        weapon[0] + armor[0] + sum(r[0] for r in rings)
        for weapon, armor, rings in product(WEAPONS, ARMOR, combinations(RINGS, 2))
        if (BOSS_HP // attack(weapon[1], (r[1] for r in rings), BOSS_ARMOR))
        > (100 // defend(armor[2], (r[2] for r in rings), BOSS_DAMAGE))
    )


print(f"Part 1: {part_one()}")  # 91
print(f"Part 2: {part_two()}")  # 158
