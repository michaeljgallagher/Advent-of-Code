import re


class Group:
    def __init__(
        self,
        army,
        units,
        hp,
        attack_dmg,
        attack_type,
        initiative,
        weaknesses,
        immunities,
    ):
        self.army = army
        self.units = units
        self.hp = hp
        self.attack_dmg = attack_dmg
        self.attack_type = attack_type
        self.initiative = initiative
        self.weaknesses = weaknesses
        self.immunities = immunities

    def effective_power(self):
        return self.units * self.attack_dmg

    def damage_to(self, target):
        if self.attack_type in target.immunities:
            return 0
        dmg = self.effective_power()
        if self.attack_type in target.weaknesses:
            dmg *= 2
        return dmg

    def take_damage(self, damage):
        killed = min(damage // self.hp, self.units)
        self.units -= killed
        return killed


def parse_input():
    with open("24.txt") as f:
        data = f.read()
    lines = data.strip().splitlines()
    groups = []
    army = None
    for line in lines:
        if line.startswith("Immune System:"):
            army = "immune"
        elif line.startswith("Infection:"):
            army = "infection"
        elif line.strip():
            match = re.match(
                r"(\d+) units each with (\d+) hit points (.*)with an attack that does (\d+) (\w+) damage at initiative (\d+)",
                line,
            )
            if match:
                units = int(match.group(1))
                hp = int(match.group(2))
                special = match.group(3)
                attack_dmg = int(match.group(4))
                attack_type = match.group(5)
                initiative = int(match.group(6))
                weaknesses = []
                immunities = []
                if special.strip():
                    special = special.strip().strip("()")
                    parts = special.split(";")
                    for part in parts:
                        part = part.strip()
                        if part.startswith("weak to"):
                            weaknesses = [x.strip() for x in part[7:].split(",")]
                        elif part.startswith("immune to"):
                            immunities = [x.strip() for x in part[9:].split(",")]
                groups.append(
                    Group(
                        army,
                        units,
                        hp,
                        attack_dmg,
                        attack_type,
                        initiative,
                        weaknesses,
                        immunities,
                    )
                )
    return groups


def simulate(groups):
    while True:
        immune = [g for g in groups if g.army == "immune" and g.units > 0]
        infection = [g for g in groups if g.army == "infection" and g.units > 0]
        if not immune or not infection:
            break
        groups_sorted = sorted(
            groups, key=lambda g: (g.effective_power(), g.initiative), reverse=True
        )
        targets = {}
        targeted = set()
        for group in groups_sorted:
            if group.units <= 0:
                continue
            enemies = [
                g
                for g in groups
                if g.army != group.army and g.units > 0 and g not in targeted
            ]
            if not enemies:
                continue
            best_target = None
            best_damage = 0
            for enemy in enemies:
                damage = group.damage_to(enemy)
                if damage > best_damage or (
                    damage == best_damage
                    and best_target
                    and (
                        enemy.effective_power() > best_target.effective_power()
                        or (
                            enemy.effective_power() == best_target.effective_power()
                            and enemy.initiative > best_target.initiative
                        )
                    )
                ):
                    best_damage = damage
                    best_target = enemy
            if best_damage > 0:
                targets[group] = best_target
                targeted.add(best_target)
        attackers = sorted(targets.keys(), key=lambda g: g.initiative, reverse=True)
        total_killed = 0
        for attacker in attackers:
            if attacker.units <= 0:
                continue
            target = targets[attacker]
            damage = attacker.damage_to(target)
            killed = target.take_damage(damage)
            total_killed += killed
        if total_killed == 0:
            return None
    return sum(g.units for g in groups if g.units > 0)


def part_one():
    groups = parse_input()
    return simulate(groups)


def part_two():
    boost = 0
    while True:
        groups = parse_input()
        for g in groups:
            if g.army == "immune":
                g.attack_dmg += boost
        result = simulate(groups)
        if result is not None:
            immune_units = sum(
                g.units for g in groups if g.army == "immune" and g.units > 0
            )
            if immune_units > 0:
                return immune_units
        boost += 1


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
