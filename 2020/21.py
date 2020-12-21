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
    res = defaultdict(set)
    for i in range(len(ingredients)):
        for allergen in allergens[i]:
            if not res[allergen]:
                res[allergen] = set(ingredients[i])
            else:
                res[allergen] &= set(ingredients[i])
    return res


alg_map = make_allergen_mapping(ingredients, allergens)


def part_one(ing_count, alg_map):
    alg_set = set(alg for v in alg_map.values() for alg in v)
    res = 0
    for ing in list(ing_count):
        if ing not in alg_set:
            res += ing_count[ing]
    return res


def part_two():
    # created the rest of the mapping by hand
    alg_map = {
        'wheat': 'nckqzsg',
        'eggs': 'xxscc',
        'fish': 'mjmqst',
        'nuts': 'gzxnc',
        'peanuts': 'vvqj',
        'shellfish': 'gbcjqbm',
        'soy': 'dllbjr',
        'sesame': 'trnnvn'
        }
    res = []
    for ing in sorted(list(alg_map)):
        res.append(alg_map[ing])
    return ','.join(res)


print(f'Part 1: {part_one(ing_count, alg_map)}')  # 1958
print(f'Part 2: {part_two()}')  # xxscc,mjmqst,gzxnc,vvqj,trnnvn,gbcjqbm,dllbjr,nckqzsg
