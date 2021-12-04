with open('04.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    data = raw_data.split('\n')
    bingo_numbers = list(map(int, data[0].split(',')))
    cards = []
    card = []
    for row in data[2:]:
        if row == '':
            cards.append(card)
            card = []
        else:
            card.append(list(map(int, row.split())))
    if card:
        cards.append(card)
    return bingo_numbers, cards


bingo_numbers, cards = parse_input(raw_data)


def check_rows(card):
    return any(all(x == 'X' for x in row) for row in card)


def check_card_win(card):
    transpose = list(map(list, zip(*card)))
    return check_rows(card) or check_rows(transpose)


def check_card_number(card, x):
    for i, row in enumerate(card):
        for j, v in enumerate(row):
            if v == x:
                card[i][j] = 'X'
    return card


def sum_card(card):
    return sum(sum(x for x in row if type(x) == int) for row in card)


def part_one(bingo_numbers, cards):
    for num in bingo_numbers:
        for i, card in enumerate(cards):
            cur = check_card_number(card, num)
            if check_card_win(cur):
                return sum_card(cur) * num
            cards[i] = cur


def part_two(bingo_numbers, cards):
    winners = set()
    for num in bingo_numbers:
        for i, card in enumerate(cards):
            if i in winners:
                continue
            cur = check_card_number(card, num)
            if check_card_win(cur):
                if len(winners) == len(cards) - 1:
                    return sum_card(cur) * num
                winners.add(i)
            cards[i] = cur


print(f'Part 1: {part_one(bingo_numbers, cards)}')  # 50008
print(f'Part 2: {part_two(bingo_numbers, cards)}')  # 17408
