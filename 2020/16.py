import re
from functools import reduce

with open('16.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    data = data.split('\n')
    rules = [list(map(int, re.findall('\d+', line))) for line in data[:20]]
    my_ticket = [int(x) for x in data[22].split(',')]
    tickets = [list(map(int, line.split(','))) for line in data[25:]]
    return rules, my_ticket, tickets


def parse_rules(rules):
    res, union = {}, set()
    for i, line in enumerate(rules):
        a, b, c, d = line
        cur = set(range(a, b+1)) | set(range(c, d+1))
        res[i] = cur
        union |= cur
    return res, union


rules, my_ticket, tickets = parse_input(data)
rules, union = parse_rules(rules)


def part_one(tickets, union):
    return sum(n for ticket in tickets for n in ticket if n not in union)


def check_ticket(ticket, union):
    return all(n in union for n in ticket)


def find_valid_fields(ticket, rules):
    res = [set() for _ in range(len(ticket))]
    for i, v in enumerate(ticket):
        for j, valid_range in rules.items():
            if v in valid_range:
                res[i].add(j)
    return res


def part_two(my_ticket, tickets, rules, union):
    valid = [ticket for ticket in tickets if check_ticket(ticket, union)]

    fields = find_valid_fields(my_ticket, rules)
    for ticket in valid:
        fields = [x&y for x, y in zip(fields, find_valid_fields(ticket, rules))]
    
    res = [(i, v) for i, v in enumerate(fields)]
    res.sort(key=lambda x: len(x[1]), reverse=True)
    for i, v in enumerate(res[:-1]):
        res[i] = (v[0], v[1] - res[i+1][1])

    key = {list(v)[0]: k for k, v in res}
    
    return reduce(lambda x, y: x*y, [my_ticket[key[i]] for i in range(6)])


print(f'Part 1: {part_one(tickets, union)}')  # 25059
print(f'Part 2: {part_two(my_ticket, tickets, rules, union)}')  # 3253972369789
