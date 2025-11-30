import re
from functools import cache
from math import prod


def parse_input():
    with open("19.txt", "r") as file:
        data = file.read()
    return [tuple(map(int, re.findall(r"\d+", row))) for row in data.splitlines()]


# 0: blueprint number
# 1: ore robot ore
# 2: clay robot ore
# 3: obsidian robot ore
# 4: obsidian robot clay
# 5: geode robot ore
# 6: geode robot obsidian


def solve(blueprint, minutes):
    max_ore_needed = max(blueprint[1], blueprint[2], blueprint[3], blueprint[5])
    max_clay_needed = blueprint[4]
    max_obsidian_needed = blueprint[6]
    res = 0

    @cache
    def dfs(
        time,
        ore,
        clay,
        obsidian,
        geodes,
        ore_robots,
        clay_robots,
        obsidian_robots,
        geode_robots,
    ):
        nonlocal res
        if time == 0:
            res = max(res, geodes)
            return

        potential = geodes + (geode_robots * time) + (time * (time - 1) // 2)
        if potential <= res:
            return

        new_ore = ore + ore_robots
        new_clay = clay + clay_robots
        new_obsidian = obsidian + obsidian_robots
        new_geodes = geodes + geode_robots

        # build geode robot
        if ore >= blueprint[5] and obsidian >= blueprint[6]:
            dfs(
                time - 1,
                new_ore - blueprint[5],
                new_clay,
                new_obsidian - blueprint[6],
                new_geodes,
                ore_robots,
                clay_robots,
                obsidian_robots,
                geode_robots + 1,
            )
            return

        # build obsidian robot
        if (
            obsidian_robots < max_obsidian_needed
            and ore >= blueprint[3]
            and clay >= blueprint[4]
        ):
            dfs(
                time - 1,
                new_ore - blueprint[3],
                new_clay - blueprint[4],
                new_obsidian,
                new_geodes,
                ore_robots,
                clay_robots,
                obsidian_robots + 1,
                geode_robots,
            )

        # build clay robot
        if clay_robots < max_clay_needed and ore >= blueprint[2]:
            dfs(
                time - 1,
                new_ore - blueprint[2],
                new_clay,
                new_obsidian,
                new_geodes,
                ore_robots,
                clay_robots + 1,
                obsidian_robots,
                geode_robots,
            )

        # build ore robot
        if ore_robots < max_ore_needed and ore >= blueprint[1]:
            dfs(
                time - 1,
                new_ore - blueprint[1],
                new_clay,
                new_obsidian,
                new_geodes,
                ore_robots + 1,
                clay_robots,
                obsidian_robots,
                geode_robots,
            )

        # don't build anything
        dfs(
            time - 1,
            new_ore,
            new_clay,
            new_obsidian,
            new_geodes,
            ore_robots,
            clay_robots,
            obsidian_robots,
            geode_robots,
        )

    dfs(minutes, 0, 0, 0, 0, 1, 0, 0, 0)
    return res


def part_one():
    blueprints = parse_input()
    return sum(i * solve(bp, 24) for i, bp in enumerate(blueprints, start=1))


def part_two():
    blueprints = parse_input()[:3]
    return prod(solve(bp, 32) for bp in blueprints)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
