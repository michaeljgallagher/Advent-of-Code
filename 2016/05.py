import hashlib

DOOR_ID = "abbhdwsy"


def md5(s):
    return hashlib.md5(s.encode()).hexdigest()


def part_one():
    password = []
    i = 0
    while len(password) < 8:
        h = md5(DOOR_ID + str(i))
        if h.startswith("00000"):
            password.append(h[5])
        i += 1
    return "".join(password)


def part_two():
    password = [None] * 8
    i = 0
    while None in password:
        h = md5(DOOR_ID + str(i))
        if (
            h.startswith("00000")
            and h[5].isdigit()
            and int(h[5]) < 8
            and password[int(h[5])] is None
        ):
            password[int(h[5])] = h[6]
        i += 1
    return "".join(password)


print(f"Part 1: {part_one()}")  # 801b56a7
print(f"Part 2: {part_two()}")  # 424a0197
