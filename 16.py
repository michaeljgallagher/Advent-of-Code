import numpy as np

with open('16.txt') as data:
    data = data.read().strip()


def fft(number):
    num = str(number)
    arr = np.array(list(num), dtype='int')
    base = [0, 1, 0, -1]
    res = ''
    for i in range(1, len(num)+1):
        pattern = []
        for b in base:
            for _ in range(i):
                pattern.append(b)
        if len(pattern)-1 < len(num):
            pattern *= (len(num) // len(pattern)) + 1
        pattern = np.array(pattern[1:(len(num)+1)])
        res += str(abs(sum(arr * pattern)) % 10)
    return res


# Part 1
number = data
for _ in range(100):
    number = fft(number)
print(f'Part 1: {number[:8]}')  # 89576828

# Part 2
'''data = '03036732577212944063491565474664'
offset = int(data[:7])
number = data * 10000
for _ in range(100):
    number = fft(number)
print(f'Part 2: {number[offset:offset+8]}')'''
