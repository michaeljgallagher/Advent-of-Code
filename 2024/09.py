from collections import deque


def parse_input():
    with open("09.txt", "r") as file:
        data = file.read().strip()
    return list(map(int, data))


DISK_MAP = parse_input()


def read_memory():
    files, free = deque(), deque()
    pos = 0
    for i, v in enumerate(DISK_MAP):
        if i & 1 == 0:
            files.append([i >> 1, v, pos])
        else:
            free.append([v, pos])
        pos += v
    return files, free


def part_one():
    files, free = read_memory()
    layout = []
    while files and free:
        layout.append(files.popleft()[:2])
        space, _ = free.popleft()
        cur = 0
        while files and cur < space:
            fid, n, _ = files.pop()
            cur += n
            if cur > space:
                files.append((fid, cur - space, None))
                layout.append((fid, n - (cur - space)))
            else:
                layout.append((fid, n))

    res = 0
    pos = 0
    for fid, sz in layout:
        res += (2 * pos + sz - 1) * sz * fid >> 1
        pos += sz
    return res


def part_two():
    files, free = read_memory()
    for file in reversed(files):
        for space in free:
            if file[2] < space[1]:
                break
            if file[1] <= space[0]:
                file[2] = space[1]
                space[1] += file[1]
                space[0] -= file[1]
                break
    return sum((2 * pos + sz - 1) * sz * fid >> 1 for fid, sz, pos in files)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
