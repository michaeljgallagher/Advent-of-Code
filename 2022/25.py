def parse_input():
    with open("25.txt", "r") as file:
        data = file.read()
    return data.splitlines()


DIGITS = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}


def convert_snafu(x):
    res = 0
    for i, c in enumerate(reversed(x)):
        res += DIGITS[c] * 5**i
    return res


def convert_digit(x):
    if x == 0:
        return ""
    match x % 5:
        case 0:
            return convert_digit(x // 5) + "0"
        case 1:
            return convert_digit(x // 5) + "1"
        case 2:
            return convert_digit(x // 5) + "2"
        case 3:
            return convert_digit((x + 2) // 5) + "="
        case 4:
            return convert_digit((x + 1) // 5) + "-"


def part_one():
    total = sum(map(convert_snafu, parse_input()))
    return convert_digit(total)


print(f"Part 1: {part_one()}")
