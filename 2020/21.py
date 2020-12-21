import re
from collections import defaultdict

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
    res = defaultdict(int)
    for row in ingredients:
        for ing in row:
            res[ing] += 1
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
    res = 0
    for ing in list(ing_count):
        if ing not in alg_set:
            res += ing_count[ing]
    return res


def part_two(alg_map):
    res = []
    for ing in sorted(list(alg_map)):
        res.append(alg_map[ing])
    return ','.join(res)


print(f'Part 1: {part_one(ing_count, alg_map)}')  # 1958
print(f'Part 2: {part_two(alg_map)}')  # xxscc,mjmqst,gzxnc,vvqj,trnnvn,gbcjqbm,dllbjr,nckqzsg
