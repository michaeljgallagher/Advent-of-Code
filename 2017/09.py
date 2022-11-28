with open("09.txt", "r") as file:
    data = file.read().strip()


def clean_garbage(s):
    garbage = False
    cleaned = ""
    removed = 0
    i = 0
    while i < len(s):
        if s[i] == "!":
            i += 1
        elif s[i] == "<" and not garbage:
            garbage = True
        elif s[i] == ">" and garbage:
            garbage = False
        elif garbage:
            removed += 1
        else:
            cleaned += s[i]
        i += 1
    return cleaned, removed


def score(s):
    score = depth = 0
    for c in s:
        score += depth * (c == "}")
        depth += 1 if c == "{" else -1 if c == "}" else 0
    return score


CLEANED, REMOVED = clean_garbage(data)

print(f"Part 1: {score(CLEANED)}")  # 12396
print(f"Part 2: {REMOVED}")  # 6346
