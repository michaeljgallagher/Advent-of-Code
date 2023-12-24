from itertools import combinations

import sympy

with open("24.txt", "r") as file:
    data = file.read().strip()

HAIL = [
    (tuple(map(int, p.split(", "))), tuple(map(int, v.split(", "))))
    for row in data.split("\n")
    for p, v in [row.split(" @ ")]
]


def check_intersect(a, b):
    (apx, apy, apz), (avx, avy, avz) = a
    (bpx, bpy, bpz), (bvx, bvy, bvz) = b
    am = avy / avx
    ac = apy - am * apx
    bm = bvy / bvx
    bc = bpy - bm * bpx
    if am == bm:
        return False
    x = (ac - bc) / (bm - am)
    y = am * x + ac
    if (
        (avx >= 0 and x < apx)
        or (avx < 0 and x > apx)
        or (bvx >= 0 and x < bpx)
        or (bvx < 0 and x > bpx)
    ):
        return False
    if 2e14 <= x <= 4e14 and 2e14 <= y <= 4e14:
        return True
    return False


def part_one():
    return sum(check_intersect(a, b) for a, b in combinations(HAIL, 2))


def part_two():
    x, v_x, y, v_y, z, v_z = sympy.symbols("x, v_x, y, v_y, z, v_z")
    eqs = []
    for i, (p, v) in enumerate(HAIL[:3]):
        (px, py, pz), (vx, vy, vz) = p, v
        t = sympy.var(f"t{i}")
        eqs.append(sympy.Eq(x + v_x * t, px + vx * t))
        eqs.append(sympy.Eq(y + v_y * t, py + vy * t))
        eqs.append(sympy.Eq(z + v_z * t, pz + vz * t))
    res = sympy.solve(eqs).pop()
    return sum(res[c] for c in (x, y, z))


print(f"Part 1: {part_one()}")  # 20847
print(f"Part 2: {part_two()}")  # 908621716620524
