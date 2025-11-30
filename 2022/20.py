import re


def parse_input():
    with open("20.txt", "r") as file:
        data = file.read()
    return list(map(int, re.findall(r"-?\d+", data)))


def mix(data, rounds=1):
    nums = list(enumerate(data))
    for _ in range(rounds):
        for i in range(len(data)):
            for j, (orig_idx, val) in enumerate(nums):
                if orig_idx == i:
                    place = j
                    to_move = val
                    break
            nums.pop(place)
            new_place = (place + to_move) % len(nums)
            nums.insert(new_place, (i, to_move))
    return nums


def part_one():
    data = parse_input()
    mixed = mix(data)
    values = [val for _, val in mixed]
    zero_idx = values.index(0)
    coords = [
        values[(zero_idx + 1000) % len(values)],
        values[(zero_idx + 2000) % len(values)],
        values[(zero_idx + 3000) % len(values)],
    ]
    return sum(coords)


def part_two():
    data = parse_input()
    decryption_key = 811589153
    encrypted = [x * decryption_key for x in data]
    mixed = mix(encrypted, rounds=10)
    values = [val for _, val in mixed]
    zero_idx = values.index(0)
    coords = [
        values[(zero_idx + 1000) % len(values)],
        values[(zero_idx + 2000) % len(values)],
        values[(zero_idx + 3000) % len(values)],
    ]
    return sum(coords)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
