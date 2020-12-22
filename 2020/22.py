from collections import deque

with open('22.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    player_one = deque([int(n) for n in data.split('\n')[1:26]])
    player_two = deque([int(n) for n in data.split('\n')[28:]])
    return player_one, player_two


def part_one(p1, p2):
    while p1 and p2:
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 > c2:
            p1 += deque([c1, c2])
        else:
            p2 += deque([c2, c1])
    winner = p1 or p2
    res = 0
    for i in range(1, len(winner)+1):
        cur = winner.pop()
        res += (i * cur)
    return res


def part_two(p1, p2):
    def recurse(p1, p2, seen):
        while (p1 and p2):
            if (tuple(p1), tuple(p2)) in seen:
                return 1, p1
            seen.add((tuple(p1), tuple(p2)))
            c1, c2 = p1.popleft(), p2.popleft()
            if c1 <= len(p1) and c2 <= len(p2):
                sp1, sp2 = deque(list(p1)[:c1]), deque(list(p2)[:c2])
                winner, _ = recurse(sp1, sp2, set())
            else:
                winner = 1 if c1 > c2 else 0
            if winner == 1:
                p1 += deque([c1, c2])
            else:
                p2 += deque([c2, c1])
        return (1, p1) if p1 else (0, p2)
    
    winner = recurse(p1, p2, set())[1]
    res = 0
    for i in range(1, len(winner)+1):
        cur = winner.pop()
        res += (i * cur)
    return res

p1, p2 = parse_input(data)
print(f'Part 1: {part_one(p1, p2)}')  # 33473
p1, p2 = parse_input(data)
print(f'Part 2: {part_two(p1, p2)}')  # 31793
