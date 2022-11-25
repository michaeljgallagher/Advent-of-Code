import hashlib
from functools import cache

SALT = "zpqevtbw"


def md5(s):
    return hashlib.md5(s.encode()).hexdigest()


@cache
def get_hash(salt, i):
    return md5(salt + str(i))


@cache
def get_stretch_hash(salt, i):
    h = get_hash(salt, i)
    for _ in range(2016):
        h = md5(h)
    return h


@cache
def get_triple(h):
    for i in range(len(h) - 2):
        if h[i] == h[i + 1] == h[i + 2]:
            return h[i]
    return None


@cache
def get_quintuple(h, c):
    return c * 5 in h


def get_keys(salt, get_hash):
    keys = []
    i = 0
    while len(keys) < 64:
        h = get_hash(salt, i)
        c = get_triple(h)
        if c:
            for j in range(i + 1, i + 1001):
                if get_quintuple(get_hash(salt, j), c):
                    keys.append(i)
                    break
        i += 1
    return keys


print(f"Part 1: {get_keys(SALT, get_hash)[-1]}")  # 16106
print(f"Part 2: {get_keys(SALT, get_stretch_hash)[-1]}")  # 22423
