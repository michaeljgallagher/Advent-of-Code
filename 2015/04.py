from hashlib import md5

BASE = "yzbqklnj"


def bruce_force(n):
    i = 0
    while True:
        cur = BASE + str(i)
        cur = cur.encode("utf-8")
        if md5(cur).hexdigest().startswith("0" * n):
            return i
        i += 1


print(f"Part 1: {bruce_force(5)}")  # 282749
print(f"Part 2: {bruce_force(6)}")  # 9962624
