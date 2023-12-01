NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("01.txt", "r") as file:
    values = file.read().strip().split("\n")


def solve(value, pt2=False):
    res = []
    for i, v in enumerate(value):
        if v.isdigit():
            res.append(v)
        if pt2:
            for j, num in enumerate(NUMBERS, start=1):
                if value[i : i + len(num)] == num:
                    res.append(str(j))
    return int(res[0] + res[-1])


print(f"Part 1: {sum(solve(val) for val in values)}")  # 55108
print(f"Part 2: {sum(solve(val, pt2=True) for val in values)}")  # 56324
