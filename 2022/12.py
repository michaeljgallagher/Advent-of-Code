from collections import deque


def parse_grid(data):
    grid = [list(line) for line in data.split("\n")]
    a_list = []
    start = end = None
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == "S":
                start = (i, j)
                a_list.append((i, j))
                grid[i][j] = "a"
            elif v == "E":
                end = (i, j)
                grid[i][j] = "z"
            elif v == "a":
                a_list.append((i, j))
    return grid, start, end, a_list


def bfs(grid, starts, end):
    seen = set()
    q = deque([(start, 0) for start in starts])
    while q:
        pos, dist = q.popleft()
        if pos == end:
            return dist
        if pos in seen:
            continue
        seen.add(pos)
        x, y = pos
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if (
                0 <= x + dx < len(grid)
                and 0 <= y + dy < len(grid[0])
                and ord(grid[x + dx][y + dy]) - ord(grid[x][y]) <= 1
            ):
                q.append(((x + dx, y + dy), dist + 1))
    return float("inf")


with open("12.txt", "r") as file:
    data = file.read().strip()

GRID, START, END, A_LIST = parse_grid(data)


def part_one():
    return bfs(GRID, [START], END)


def part_two():
    return bfs(GRID, A_LIST, END)


print(f"Part 1: {part_one()}")  # 339
print(f"Part 2: {part_two()}")  # 332
