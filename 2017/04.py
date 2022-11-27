with open("04.txt", "r") as file:
    data = file.read().strip()


def is_valid(passphrase):
    words = passphrase.split()
    return len(words) == len(set(words))


def is_valid_anagram(passphrase):
    words = passphrase.split()
    return len(words) == len(set(map(lambda w: "".join(sorted(w)), words)))


def part_one(data):
    return sum(is_valid(passphrase) for passphrase in data.split("\n"))


def part_two(data):
    return sum(is_valid_anagram(passphrase) for passphrase in data.split("\n"))


print(f"Part 1: {part_one(data)}")  # 325
print(f"Part 2: {part_two(data)}")  # 119
