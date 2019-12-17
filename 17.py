s = '''..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..'''

s = s.split()


def find_intersections(grid):
    intersections = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            one, two, thr, fou = 0, 0, 0, 0
            if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[i])-1:
                continue
            else:
                if grid[i][j] == '#':
                    one = grid[i+1][j] == '#'
                    two = grid[i-1][j] == '#'
                    thr = grid[i][j+1] == '#'
                    fou = grid[i][j-1] == '#'
                    if int(one) + int(two) + int(thr) + int(fou) >= 3:
                        intersections.append((j, i))
    return intersections


def part_one(intersections):
    res = 0
    for x in intersections:
        res += x[0] * x[1]
    return res


print(f'Part 1: {part_one(find_intersections(s))}')
