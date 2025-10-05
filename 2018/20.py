import heapq


def parse_input():
    with open("20.txt", "r") as file:
        data = file.read()
    return data.strip("^$").splitlines().pop()


def find_doors():
    regex = parse_input()
    doors = set()
    stack = []
    x, y = 0, 0
    for c in regex:
        if c in "NEWS":
            match c:
                case "N":
                    nx, ny = x, y - 1
                case "E":
                    nx, ny = x + 1, y
                case "W":
                    nx, ny = x - 1, y
                case "S":
                    nx, ny = x, y + 1
            doors.add((min(x, nx), min(y, ny), max(x, nx), max(y, ny)))
            x, y = nx, ny
        elif c == "(":
            stack.append((x, y))
        elif c == "|":
            x, y = stack[-1]
        elif c == ")":
            stack.pop()
    return doors


def solve(pt2=False):
    doors = find_doors()
    seen = set()
    heap = [(0, 0, 0)]
    cnt = 0
    while heap:
        d, x, y = heapq.heappop(heap)
        seen.add((x, y))
        if d >= 1000:
            cnt += 1
        for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
            if ((min(x, nx), min(y, ny), max(x, nx), max(y, ny)) in doors) and (
                (nx, ny) not in seen
            ):
                heapq.heappush(heap, (d + 1, nx, ny))
        if not heap:
            return cnt if pt2 else d


print(f"Part 1: {solve()}")
print(f"Part 2: {solve(pt2=True)}")
