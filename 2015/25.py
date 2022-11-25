START = 20151125
BASE = 252533
MOD = 33554393
ROW = 2947
COL = 3029


def get_exp(r, c):
    return ((r + c - 1) * (r + c - 2) >> 1) + c


def solve(base, exp, mod):
    res = 1
    while exp:
        if exp & 1:
            _, res = divmod(res * base, mod)
        exp >>= 1
        base = base * base % mod
    return res * START % mod


print(f"Part 1: {solve(BASE, get_exp(ROW, COL) - 1, MOD)}")  # 19980801
