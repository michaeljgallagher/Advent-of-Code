from collections import Counter

with open('08.txt', 'r') as data:
    data = data.read().strip()


def find_layers(s, width, height):
    pointer = 0
    w, h = width, height
    layers = []
    while pointer < len(s):
        layer = []
        for _ in range(h):
            layer.append(list(s[pointer:pointer+w]))
            pointer += w
        layers.append(layer)
    return layers


def find_min_zeros(image):
    min_zeros = (float('Inf'), 0)  # number of zeros, layer index
    for i in range(len(image)):
        c = Counter()
        for line in image[i]:
            c += Counter(line)
        if c['0'] < min_zeros[0]:
            min_zeros = (c['0'], i)
    return min_zeros


def calc_part1(image, layer):
    c = Counter()
    for line in image[layer]:
        c += Counter(line)
    return c['1'] * c['2']


image = find_layers(data, 25, 6)
layer = find_min_zeros(image)[1]
print(calc_part1(image, layer))  # 1224


def decode_image(image, width, height):
    final_image = [['.' for _ in range(width)] for _ in range(height)]
    for layer in image:
        for i in range(height):
            for j in range(width):
                if layer[i][j] == '1' and final_image[i][j] == '.':
                    final_image[i][j] = '|'
                if layer[i][j] == '0' and final_image[i][j] == '.':
                    final_image[i][j] = ' '
    for row in final_image:
        print(''.join(row))


decode_image(image, 25, 6)  # EBZUR
