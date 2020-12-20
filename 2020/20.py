with open('20.txt', 'r') as file:
    data = file.read()


def transpose(tile):
    return [''.join(row) for row in zip(*tile)]


def reverse_tile(tile):
    return [''.join(reversed(row)) for row in tile]


def rotate(tile):
    res = [tile]
    for _ in range(3):
        res.append(reverse_tile(transpose(res[-1])))
    return res


def translations(tile):
    return rotate(tile) + rotate(transpose(tile))


def parse_input(data):
    tiles = {}
    for tile in data.split('\n\n'):
        cur = tile.split('\n')
        n = int(cur[0][-5:-1])
        tiles[n] = translations(cur[1:])
    return tiles


tiles = parse_input(data)
image = [[0] * 12 for _ in range(12)]
stack = [(r,c) for c in range(11,-1,-1) for r in range(11,-1,-1)]


def make_image(stack):
    if not stack:
        return True
    r, c = stack.pop()
    for n in list(tiles):
        cur = tiles[n]
        del tiles[n]
        for tile in cur:
            if r and image[r - 1][c][1][-1] != tile[0]:
                continue
            if c and [row[-1] for row in image[r][c - 1][1]] != [row[0] for row in tile]:
                continue
            image[r][c] = (n, tile)
            if make_image(stack):
                return True
        tiles[n] = cur
    stack.append((r, c))


make_image(stack)


def part_one(image):
    return image[0][0][0] * image[0][-1][0] * image[-1][0][0] * image[-1][-1][0]


def remove_border(tile):
    return [row[1:-1] for row in tile[1:-1]]


trimmed = [[remove_border(tile[1]) for tile in row] for row in image]
grid = []
for i in range(12):
    for k in range(8):
        cur = []
        for j in range(12):
            cur.append(trimmed[i][j][k])
        grid.append(''.join(cur))

monster = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.split('\n')


def part_two(grid, monster):
    count_grid = ''.join(grid).count('#')
    count_monster = ''.join(monster).count('#')
    res = 0
    for mon in translations(monster):
        cur = 0
        for dr in range(len(grid) - len(mon) + 1):
            for dc in range(len(grid[0]) - len(mon[0]) + 1):
                if all(mon[r][c] == ' ' or grid[r + dr][c + dc] == '#' for r in range(len(mon)) for c in range(len(mon[0]))):
                    cur += 1
        res = max(res, cur)
    return count_grid - (res * count_monster)
    

print(f'Part 1: {part_one(image)}')  # 23386616781851
print(f'Part 2: {part_two(grid, monster)}')  # 2376
