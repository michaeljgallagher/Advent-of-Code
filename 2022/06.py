with open("06.txt", "r") as file:
    data = file.read().strip()


def find_substring(data, n):
    cur = data[:n]
    i = n
    while i < len(data):
        if len(set(cur)) == n:
            return i
        cur = cur[1:] + data[i]
        i += 1


print(f"Part 1: {find_substring(data, 4)}")  # 1779
print(f"Part 2: {find_substring(data, 14)}")  # 2635
