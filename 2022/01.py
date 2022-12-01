with open("01.txt", "r") as file:
    data = file.read().strip()

ELVES = sorted(
    sum(int(x) for x in elf.split("\n"))
    for elf in data.split("\n\n")
)

print(f"Part 1: {ELVES[-1]}")  # 71502
print(f"Part 2: {sum(ELVES[-3:])}")  # 208191
