with open("15.txt", "r") as file:
    data = file.read().strip()


def hash(s):
    res = 0
    for c in s:
        res = (res + ord(c)) * 17 % 256
    return res


def find_index(label, box):
    for i, (lab, _) in enumerate(box):
        if lab == label:
            return i
    return len(box)


def hashmap(s, boxes):
    if "-" in s:
        label, _ = s.split("-")
        k = hash(label)
        i = find_index(label, boxes[k])
        if i != len(boxes[k]):
            boxes[k].pop(i)
    else:
        label, focal_len = s.split("=")
        k = hash(label)
        i = find_index(label, boxes[k])
        if i != len(boxes[k]):
            boxes[k][i] = (label, focal_len)
        else:
            boxes[k].append((label, focal_len))


def part_one():
    return sum(hash(s) for s in data.split(","))


def part_two():
    boxes = [[] for _ in range(256)]
    for s in data.split(","):
        hashmap(s, boxes)
    return sum(
        i * j * int(focal_len)
        for i, box in enumerate(boxes, start=1)
        for j, (label, focal_len) in enumerate(box, start=1)
    )


print(f"Part 1: {part_one()}")  # 507666
print(f"Part 2: {part_two()}")  # 233537
