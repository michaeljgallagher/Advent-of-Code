import re
from collections import defaultdict, Counter

with open('21.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    ingredients, allergens = [], []
    for line in data.split('\n'):
        m = re.findall(r'(.*) \(contains (.*)\)', line)
        ingredients.append(m[0][0].split(' '))
        allergens.append(m[0][1].split(', '))
    return ingredients, allergens


ingredients, allergens = parse_input(data)


def count_ings(ingredients):
    res = Counter()
    for row in ingredients:
        res += Counter(row)
    return res


ing_count = count_ings(ingredients)


def make_allergen_mapping(ingredients, allergens):
    possible = defaultdict(set)
    for i in range(len(ingredients)):
        for allergen in allergens[i]:
            if not possible[allergen]:
                possible[allergen] = set(ingredients[i])
            else:
                possible[allergen] &= set(ingredients[i])
    used = set()
    res = {}
    while len(used) < len(possible):
        for alg, ing in possible.items():
            if len(ing - used) == 1:
                cur = list(ing-used)[0]
                res[alg] = cur
                used.add(cur)
                break
    return res


alg_map = make_allergen_mapping(ingredients, allergens)


def part_one(ing_count, alg_map):
    alg_set = set(alg_map.values())
    return sum(ing_count[ing] for ing in ing_count if ing not in alg_set)


def part_two(alg_map):
    return ','.join(alg_map[ing] for ing in sorted(list(alg_map)))


print(f'Part 1: {part_one(ing_count, alg_map)}')  # 1958
print(f'Part 2: {part_two(alg_map)}')  # xxscc,mjmqst,gzxnc,vvqj,trnnvn,gbcjqbm,dllbjr,nckqzsg
