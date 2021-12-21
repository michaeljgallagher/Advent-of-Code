import re
from collections import deque
from functools import lru_cache
from itertools import product

with open('21.txt', 'r') as file:
    raw_data = file.read()


def parse_data(raw_data):
    return (int(x) for x in re.findall(r'position: (\d+)', raw_data))


PLAYER_ONE, PLAYER_TWO = parse_data(raw_data)


def part_one(pos_one, pos_two):
    pos = [pos_one, pos_two]
    rolls = 0
    q = deque(range(1, 101))
    score = [0, 0]
    turn = 0
    while max(score) < 1000:
        move = sum(list(q)[:3])
        q.rotate(-3)
        rolls += 3
        pos[turn] = (pos[turn] + move) % 10
        if pos[turn] == 0:
            pos[turn] = 10
        score[turn] += pos[turn]
        turn = 1 - turn
    return min(score) * rolls


def part_two(pos_one, pos_two):

    @lru_cache(None)
    def recur(pos, scores=(0, 0), turn=0):
        cur_pos, cur_scores = list(pos), list(scores)
        wins = [0, 0]
        for a, b, c in product((1, 2, 3), repeat=3):
            move = a + b + c
            cur_pos[turn] = (pos[turn] + move) % 10
            if cur_pos[turn] == 0:
                cur_pos[turn] = 10
            cur_scores[turn] = scores[turn] + cur_pos[turn]
            if cur_scores[turn] >= 21:
                wins[turn] += 1
            else:
                one, two = recur(tuple(cur_pos), tuple(cur_scores), 1-turn)
                wins[0] += one
                wins[1] += two
        return wins

    return max(recur((pos_one, pos_two)))


print(f'Part 1: {part_one(PLAYER_ONE, PLAYER_TWO)}')  # 864900
print(f'Part 2: {part_two(PLAYER_ONE, PLAYER_TWO)}')  # 575111835924670
