def parse_input():
    with open("22.txt", "r") as file:
        data = file.read()
    return data.splitlines()


def solve(pos, mod, iters=-1):
    shuffles = parse_input()
    initial = 0
    diff = 1
    for line in shuffles:
        technique, *_, n = line.split()
        if n == "stack":
            diff *= -1
            initial += diff
        elif technique == "cut":
            initial += int(n) * diff
        else:
            diff *= pow(int(n), -1, mod)
    initial *= pow(1 - diff, -1, mod)
    diff = pow(diff, iters, mod)
    return ((pos - initial) * diff + initial) % mod


print(f"Part 1: {solve(2019, 10007)}")
print(f"Part 2: {solve(2020, 119315717514047, 101741582076661)}")
