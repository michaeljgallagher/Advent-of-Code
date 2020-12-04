with open('04.txt', 'r') as file:
    data = file.read().split('\n')


def parse_input(data):
    res = []
    passport = {}
    for row in data:
        if not row:
            res.append(passport)
            passport = {}
        else:
            passport.update({k:v for k, v in [x.split(':') for x in row.split()]})
    if passport: res.append(passport)
    return res


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
    hgt = passport.get('hgt', '  ')
    if hgt[-2:] == 'cm':
        return 150 <= int(hgt[:-2]) <= 193
    if hgt[-2:] == 'in':
        return 59 <= int(hgt[:-2]) <= 76
    return False


def has_valid_hcl(passport):
    hcl = passport['hcl']
    return (
        hcl[0] == '#' and 
        len(hcl) == 7 and 
        all(x in '0123456789abcdef' for x in hcl[1:])
    )


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
    PASSPORTS = parse_input(data)
    print(f'Answer for part 1: {part1(PASSPORTS)}')  # 219
    print(f'Answer for part 2: {part2(PASSPORTS)}')  # 127
