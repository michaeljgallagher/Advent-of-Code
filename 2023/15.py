from functools import reduce

with open("15.txt", "r") as file:
    data = file.read().strip()


def hash(s):
    return reduce(lambda x, y: (x + ord(y)) * 17 % 256, s, 0)


def hashmap(s, boxes):
    match s.replace("-", "").split("="):
        case [label]:
            boxes[hash(label)].pop(label, None)
        case [label, focal_len]:
            boxes[hash(label)][label] = int(focal_len)


def part_one():
    return sum(hash(s) for s in data.split(","))


def part_two():
    boxes = [{} for _ in range(256)]
    for s in data.split(","):
        hashmap(s, boxes)
    return sum(
        i * j * focal_len
        for i, box in enumerate(boxes, start=1)
        for j, (label, focal_len) in enumerate(box.items(), start=1)
    )


print(f"Part 1: {part_one()}")  # 507666
print(f"Part 2: {part_two()}")  # 233537
