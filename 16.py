with open('16.txt') as data:
    data = list(map(int, data.read().strip()))


def fft2(number):
    length = len(number)
    copy = number[:]
    for i in range(length):
        j = i
        step = i + 1
        total = 0
        while j < length:
            total += sum(copy[j:j + step])
            j += 2 * step
            total -= sum(copy[j:j + step])
            j += 2 * step
        number[i] = abs(total) % 10
    return number


# Part 1
number = data[:]
for _ in range(100):
    number = fft2(number)
res = ''.join(map(str, number[:8]))
print(f'Part 1: {res}')  # 89576828

# Part 2
offset = int(''.join(map(str, data[:7])))
number = (data * 10000)[offset:]
length = len(number)
for _ in range(100):
    for i in range(length-2, -1, -1):
        number[i] += number[i+1]
        number[i] %= 10
res = ''.join(map(str, number[:8]))
print(f'Part 2: {res}')  # 23752579
