with open("09.txt", "r") as file:
    data = file.read().strip()


def decompress(data, version=1):
    i = 0
    res = 0
    while i < len(data):
        if data[i] == "(":
            j = data.index(")", i)
            length, repeat = map(int, data[i + 1 : j].split("x"))
            if version == 1:
                res += length * repeat
            else:
                res += decompress(data[j + 1 : j + 1 + length], version) * repeat
            i = j + 1 + length
        else:
            res += 1
            i += 1
    return res


print(f"Part 1: {decompress(data)}")  # 102239
print(f"Part 2: {decompress(data, version=2)}")  # 10780403063
