def parse_input():
    with open("17.txt", "r") as file:
        data = file.read().strip()
    return data


JETS = parse_input()
ROCKS = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # horizontal line: ####
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],  # plus sign
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # backwards L
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # vertical line
    [(0, 0), (1, 0), (0, 1), (1, 1)],  # square
]


def solve(num_rocks):
    seen = set()
    idx = 0
    res = 0
    heights = []
    states = {}
    cycle_found = False

    for i in range(num_rocks):
        rock = ROCKS[i % len(ROCKS)]
        x, y = 2, res + 4
        while True:
            jet = JETS[idx]
            idx = (idx + 1) % len(JETS)
            dx = -1 if jet == "<" else 1
            nx = x + dx
            if all(
                0 <= nx + rx < 7 and (nx + rx, y + ry) not in seen for rx, ry in rock
            ):
                x = nx
            ny = y - 1
            if ny > 0 and all((x + rx, ny + ry) not in seen for rx, ry in rock):
                y = ny
            else:
                for rx, ry in rock:
                    seen.add((x + rx, y + ry))
                    res = max(res, y + ry)
                break
        heights.append(res)
        if not cycle_found and num_rocks > 10000 and res > 100:
            profile = tuple(
                max(
                    (h for px, h in seen if px == col and h > res - 50),
                    default=0,
                )
                - res
                for col in range(7)
            )
            state = (i % len(ROCKS), idx % len(JETS), profile)
            if state in states:
                prev_rock, prev_height = states[state]
                cycle_length = i - prev_rock
                cycle_height = res - prev_height
                rem = num_rocks - i - 1
                cycles = rem // cycle_length
                leftover = rem % cycle_length
                final_height = res + cycles * cycle_height
                if leftover > 0:
                    final_height += heights[prev_rock + leftover] - heights[prev_rock]
                return final_height
            states[state] = (i, res)
    return res


print(f"Part 1: {solve(2022)}")
print(f"Part 2: {solve(1000000000000)}")
