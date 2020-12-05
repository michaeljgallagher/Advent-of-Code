import re

def parse_input(data):
    return [{k:v for k, v in [x.split(':') for x in row.split()]} for row in data]


def has_valid_fields(passport):
    valid_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return valid_fields.issubset(set(passport.keys()))


def has_valid_byr(passport):
    return 1920 <= int(passport.get('byr', -1)) <= 2002


def has_valid_iyr(passport):
    return 2010 <= int(passport.get('iyr', -1)) <= 2020


def has_valid_eyr(passport):
    return 2020 <= int(passport.get('eyr', -1)) <= 2030


def has_valid_hgt(passport):
    hgt = passport.get('hgt', ' ')
    return bool(re.match(r'1([5-8][\d]|9[0-3])cm|(59|6[\d]|7[0-6])in', hgt))


def has_valid_hcl(passport):
    hcl = passport.get('hcl', ' ')
    return bool(re.match(r'#[0-9a-f]{6}', hcl))


def has_valid_ecl(passport):
    return passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def has_valid_pid(passport):
    return len(passport['pid']) == 9 and passport['pid'].isdecimal()
    

def check_all(passport):
    checks = [has_valid_fields, has_valid_byr, has_valid_iyr, has_valid_eyr,
                has_valid_hgt, has_valid_hcl, has_valid_ecl, has_valid_pid]
    return all(func(passport) for func in checks)


def part1(passports):
    return sum(has_valid_fields(passport) for passport in passports)


def part2(passports):
    return sum(check_all(passport) for passport in passports)


if __name__ == '__main__':
    with open('04.txt', 'r') as file:
        data = file.read().split('\n\n')

    passports = parse_input(data)

    print(f'Part 1: {part1(passports)}')  # 219
    print(f'Part 2: {part2(passports)}')  # 127
