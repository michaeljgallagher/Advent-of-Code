with open('24.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    res = []
    cur = []
    for i, line in enumerate(raw_data.split('\n')):
        if i % 18 in (4, 5, 15):
            cur.append(int(line.split()[-1]))
            if len(cur) == 3:
                res.append(cur)
                cur = []
    return res


DATA = parse_input(raw_data)
for line in DATA:
    print(line)

'''
inp w
mul x 0
add x z
mod x 26
div z {a}
add x {b}
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y {c}
mul y x
add z y

input w
z //= a  # either 1 or 26
if check w != (z % 26) + b:  # when a is 1, this is always true
    z = z * 26 + w + c

input w
z //= a
if a == 1:
    z = z * 26 + w + c

===> a == 1, pushes a base-26 integer
===> a == 26, pop, if popped + b != w, then w + c is pushed onto stack
                                       we don't want that, so we want
                                       popped + b == w
                                       popped == w_prev + c_prev
                                       w == w_prev + c_prev + b

[1, 13, 0]
[1, 11, 3]
[1, 14, 8]
[26, -5, 5]
[1, 14, 13]
[1, 10, 9]
[1, 12, 6]
[26, -14, 1]
[26, -8, 1]
[1, 13, 2]
[26, 0, 7]
[26, -5, 5]
[26, -9, 8]
[26, -1, 15]

push input[0]
push input[1] + 3
push input[2] + 8
pop  input[3] == popped - 5
push input[4] + 13
push input[5] + 9
push input[6] + 6
pop  input[7] == popped - 14
pop  input[8] == popped - 8
push input[9] + 2
pop  input[10] == popped
pop  input[11] == popped - 5
pop  input[12] == popped - 9
pop  input[13] == popped - 1

input[3] = input[2] + 3
input[7] = input[6] - 8
input[8] = input[5] + 1
input[10] = input[9] + 2
input[11] = input[4] + 8
input[12] = input[1] - 6
input[13] = input[0] - 1

input[3] = input[2] + 3
input[6] = input[7] + 8
input[8] = input[5] + 1
input[10] = input[9] + 2
input[11] = input[4] + 8
input[1] = input[12] + 6
input[0] = input[13] + 1

to maximize, set all lhs to 9 and solve:
0 1 2 3 4 5 6 7 8 9 0 1 2 3
9 9 6 9 1 8 9 1 9 7 9 9 3 8

99691891979938
'''


def part_one():
    return 99691891979938


'''
input[2] = input[3] - 3
input[7] = input[6] - 8
input[5] = input[8] - 1
input[9] = input[10] - 2
input[4] = input[11] - 8
input[12] = input[1] - 6
input[13] = input[0] - 1


to minimize, set all lhs to 1 and solve:
0 1 2 3 4 5 6 7 8 9 0 1 2 3
2 7 1 4 1 1 9 1 2 1 3 9 1 1

27141191213911
'''


def part_two():
    return 27141191213911


print(f'Part 1: {part_one()}')  # 99691891979938
print(f'Part 2: {part_two()}')  # 27141191213911
