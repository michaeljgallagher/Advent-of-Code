import re
from dataclasses import dataclass
from heapq import heappop, heappush

with open("22.txt", "r") as file:
    data = file.read().strip()


@dataclass
class Spell:
    name: str
    cost: int
    damage: int = 0
    heal: int = 0
    effect: bool = False
    turns: int = 0
    armor: int = 0
    mana: int = 0

    def __hash__(self):
        return hash(self.name)


@dataclass
class State:
    hp: int
    mana: int
    armor: int
    boss_hp: int
    boss_dmg: int
    effects: dict
    mana_spent: int
    hard: bool

    def process_effects(self):
        self.armor = 0
        new_effects = {}
        for effect, timer in self.effects.items():
            self.hp += effect.heal
            self.mana += effect.mana
            self.boss_hp -= effect.damage
            self.armor = max(self.armor, effect.armor)
            if timer > 1:
                new_effects[effect] = timer - 1
        self.effects = new_effects

    def __lt__(self, other):
        return self.mana_spent < other.mana_spent

    def __hash__(self):
        return hash(
            (
                self.hp,
                self.mana,
                self.armor,
                self.boss_hp,
                self.boss_dmg,
                tuple(self.effects.items()),
            )
        )

    def __eq__(self, other):
        return (
            self.hp == other.hp
            and self.mana == other.mana
            and self.armor == other.armor
            and self.boss_hp == other.boss_hp
            and self.boss_dmg == other.boss_dmg
            and self.effects == other.effects
        )


BOSS_HP, BOSS_DMG = map(int, re.findall(r"(\d+)", data))

SPELLS = [
    Spell("Magic Missile", 53, damage=4),
    Spell("Drain", 73, damage=2, heal=2),
    Spell("Shield", 113, effect=True, turns=6, armor=7),
    Spell("Poison", 173, effect=True, turns=6, damage=3),
    Spell("Recharge", 229, effect=True, turns=5, mana=101),
]


def dijkstra(hard_mode=False):
    pq = [State(50, 500, 0, BOSS_HP, BOSS_DMG, {}, 0, hard_mode)]
    seen = set()
    while pq:
        state = heappop(pq)
        if state.boss_hp <= 0:
            return state.mana_spent
        if state in seen:
            continue
        seen.add(state)

        # player attack
        state.hp -= state.hard
        if state.hp <= 0:
            continue
        state.process_effects()
        if state.mana < 53:
            continue
        for spell in SPELLS:
            new_state = State(
                state.hp,
                state.mana,
                state.armor,
                state.boss_hp,
                state.boss_dmg,
                state.effects.copy(),
                state.mana_spent,
                state.hard,
            )
            if spell.cost > new_state.mana or spell in new_state.effects:
                continue

            if spell.effect:
                new_state.effects[spell] = spell.turns
            else:
                new_state.boss_hp -= spell.damage
                new_state.hp += spell.heal
            new_state.mana -= spell.cost
            new_state.mana_spent += spell.cost

            # boss attack
            new_state.process_effects()
            if new_state.boss_hp <= 0:
                heappush(pq, new_state)
                continue
            new_state.hp -= max(1, new_state.boss_dmg - new_state.armor)
            if new_state.hp > 0:
                heappush(pq, new_state)


print(f"Part 1: {dijkstra()}")  # 953
print(f"Part 2: {dijkstra(hard_mode=True)}")  # 1289
