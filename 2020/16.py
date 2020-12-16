import re
from collections import defaultdict
from functools import reduce

MY_TICKET = [103,197,83,101,109,181,61,157,199,137,97,179,151,89,211,59,139,149,53,107]

RULES = """departure location: 26-404 or 427-951
departure station: 43-307 or 325-967
departure platform: 39-383 or 399-950
departure track: 31-157 or 178-969
departure date: 28-109 or 135-950
departure time: 38-622 or 631-958
arrival location: 35-61 or 69-957
arrival station: 36-216 or 241-951
arrival platform: 41-586 or 606-967
arrival track: 47-573 or 586-951
class: 31-439 or 445-957
duration: 35-925 or 939-965
price: 41-473 or 494-952
route: 45-742 or 754-963
row: 41-338 or 357-952
seat: 45-848 or 873-968
train: 37-183 or 197-952
type: 46-509 or 522-974
wagon: 32-69 or 81-967
zone: 37-759 or 780-967"""


with open('16.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    return [list(map(int, line.split(','))) for line in data.split('\n')]


def parse_rules(rules):
    res = defaultdict(list)
    for i, line in enumerate(rules.split('\n')):
        m = re.findall(r"(\d+)-(\d+) or (\d+)-(\d+)", line)
        res[i].extend([(int(m[0][0]), int(m[0][1])), (int(m[0][2]), int(m[0][3]))])
    return res


def check_ticket(ticket, rules):
    for i, v in enumerate(ticket):
        flag = False
        for r1, r2 in rules.values():
            a1, b1 = r1
            a2, b2 = r2
            if v in range(a1, b1+1) or v in range(a2, b2+1):
                flag = True
                continue
        if not flag:
            return v
    return


def check_ticket_two(ticket, rules):
    res = [set() for _ in range(len(ticket))]
    for i, v in enumerate(ticket):
        for j, ranges in rules.items():
            r1, r2 = ranges
            a1, b1 = r1
            a2, b2 = r2
            if v in range(a1, b1+1) or v in range(a2, b2+1):
                res[i].add(j)
    return res


def part_one(data, rules):
    res = []
    for ticket in data:
        v = check_ticket(ticket, rules)
        if v:
            res.append(v)
    return sum(res)


def part_two(data, rules):
    valid = [ticket for ticket in data if not check_ticket(ticket, rules)]
    cur = check_ticket_two(MY_TICKET, rules)
    for ticket in valid:
        cur = [x&y for x, y in zip(cur, check_ticket_two(ticket, rules))]
    res = [(i, v) for i, v in enumerate(cur)]
    res.sort(key=lambda x: len(x[1]), reverse=True)
    for i, v in enumerate(res[:-1]):
        res[i] = (v[0], v[1] - res[i+1][1])
    order = {list(v)[0]: k for k, v in res}
    ans = [MY_TICKET[order[i]] for i in range(6)]
    return reduce(lambda x, y: x*y, ans)


data = parse_input(data)
rules = parse_rules(RULES)
print(f'Part 1: {part_one(data, rules)}')  # 25059
print(f'Part 2: {part_two(data, rules)}')  # 3253972369789
