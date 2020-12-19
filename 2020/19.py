import re

with open('19.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    rules = [line for line in data.split('\n')[:135]]
    rd = dict([line.split(': ') for line in rules])
    messages = [line for line in data.split('\n')[136:]]
    return rd, messages


rules, messages = parse_input(data)


def make_regex(n):
    rule = rules[n]
    if re.fullmatch(r'"."', rule):
        return rule[1]
    res = []
    options = rule.split(' | ')
    for opt in options:
        cur = opt.split(' ')
        new = ''.join([make_regex(x) for x in cur])
        res.append(new)
    return '(?:' + '|'.join(res) + ')'


def part_one(messages):
    regex = make_regex('0')
    return sum(1 if re.fullmatch(regex, x) else 0 for x in messages)


def part_two(messages):
    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'
    regex = make_regex('0')
    return sum(1 if re.fullmatch(regex, x) else 0 for x in messages)

print(f'Part 1: {part_one(messages)}')  # 239
print(f'Part 2: {part_two(messages)}')  # 
