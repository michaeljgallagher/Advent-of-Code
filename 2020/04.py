with open('04.txt', 'r') as file:
    data = file.read().split('\n')

# print(data)
def part1(data):
    valid = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    res = 0
    passport = {}
    for row in data:
        cur = row.split(' ')
        if cur == ['']:
            if valid.issubset(set(passport.keys())):
                res += 1
            passport = {}
            #print(passport)
        else:
            for x in cur:
                    k, v = x.split(':')
                    passport[k] = v
            #print(passport)
    return res


def checks(passport):
    valid = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    if not (valid.issubset(set(passport.keys()))):
        return False
    if not (1920 <= int(passport['byr']) <= 2002):
        return False
    if not (2010 <= int(passport['iyr']) <= 2020):
        return False
    if not (2020 <= int(passport['eyr']) <= 2030):
        return False
    if passport['hgt'][-2:] not in ['in', 'cm']:
        return False
    if passport['hgt'][-2:] == 'cm':
        if not (150 <= int(passport['hgt'][:-2]) <= 193):
            return False
    if passport['hgt'][-2:] == 'in':
        if not (59 <= int(passport['hgt'][:-2]) <= 76):
            return False
    if passport['hcl'][0] != '#':
        return False
    if not (len(passport['hcl'][1:]) == 6 and all([x in '0123456789abcdefABCDEF' for x in passport['hcl'][1:]])):
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not (len(passport['pid']) == 9 and passport['pid'].isdecimal()):
        return False
    return True

def part2(data):
    res = 0
    passport = {}
    for row in data:
        cur = row.split(' ')
        if cur == ['']:
            if checks(passport):
                res += 1
            passport = {}
        else:
            for x in cur:
                    k, v = x.split(':')
                    passport[k] = v
    return res

print(f'Answer for part 1: {part1(data)}')  # 219
print(f'Answer for part 2: {part2(data)}')  # 127
