with open("18.txt", "r") as file:
    data = file.read().strip()


def calc_row(row):
    res = []
    for i in range(len(row)):
        l = 1 if i - 1 == -1 else row[i - 1]
        c = row[i]
        r = 1 if i + 1 == len(row) else row[i + 1]
        res.append(
            int(
                (l, c, r)
                not in {(0, 0, 1), (1, 0, 0), (0, 1, 1), (1, 1, 0)}
            )
        )
    return res


def solve(data, num_rows):
    row = list(map(lambda x: int(x == "."), data))
    res = sum(row)
    for _ in range(num_rows - 1):
        row = calc_row(row)
        res += sum(row)
    return res


print(f"Part 1: {solve(data, 40)}")  # 2005
print(f"Part 2: {solve(data, 400000)}")  # 20008491
