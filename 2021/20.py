from itertools import product

with open('20.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    enhancement_algo, image = raw_data.split('\n\n')
    return enhancement_algo, [[x for x in line] for line in image.split('\n')]


enhancement_algo, IMAGE = parse_input(raw_data)


def get_surrounding(i, j, image, default='.'):
    N, M = len(image), len(image[0])
    res = []
    for di, dj in product((-1, 0, 1), repeat=2):
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M:
            res.append(image[ni][nj])
        else:
            res.append(default)
    return ''.join(res)


def get_output_pixel(s):
    idx = int(s.translate(str.maketrans('.#', '01')), 2)
    return enhancement_algo[idx]


def calc_image(image, default='.'):
    N, M = len(image), len(image[0])
    res = []
    for i in range(-3, N+3):
        cur = []
        for j in range(-3, M+3):
            s = get_surrounding(i, j, image, default)
            cur.append(get_output_pixel(s))
        res.append(cur)
    return res


def part_one():
    image = [[x for x in row] for row in IMAGE]
    for i in range(2):
        default = '#' if i & 1 else '.'
        image = calc_image(image, default)
    return sum(sum(x == '#' for x in row) for row in image)


def part_two():
    image = [[x for x in row] for row in IMAGE]
    for i in range(50):
        default = '#' if i & 1 else '.'
        image = calc_image(image, default)
    return sum(sum(x == '#' for x in row) for row in image)


print(f'Part 1: {part_one()}')  # 5354
print(f'Part 2: {part_two()}')  # 18269
