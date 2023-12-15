from functools import reduce

with open("15.txt", "r") as file:
    data = file.read().strip()


def h(s):
    return reduce(lambda x, y: (x + ord(y)) * 17 % 256, s, 0)


def hashmap(s, boxes):
    if "-" in s:
        label, _ = s.split("-")
        k = h(label)
        boxes[k].pop(label, 0)
    else:
        label, focal_len = s.split("=")
        k = h(label)
        boxes[k][label] = focal_len


def part_one():
    return sum(h(s) for s in data.split(","))


def part_two():
    boxes = [{} for _ in range(256)]
    for s in data.split(","):
        hashmap(s, boxes)
    return sum(
        i * j * int(focal_len)
        for i, box in enumerate(boxes, start=1)
        for j, (label, focal_len) in enumerate(box.items(), start=1)
    )


print(f"Part 1: {part_one()}")  # 507666
print(f"Part 2: {part_two()}")  # 233537
