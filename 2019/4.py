import re


def password_count(l, r):
    count = 0
    for i in range(l, r):
        i = str(i)
        x = re.findall(r'(.)\1+', i)
        if list(i) != sorted(list(i)):
            continue
        elif not x:
            continue
        else:
            count += 1
    return count


print(password_count(245182, 790573))  # 1099


def password_count2(l, r):
    count = 0
    for i in range(l, r):
        i = str(i)
        x = re.findall(r'(.)\1+', i)
        y = re.findall(r'(.)\1{2,5}', i)
        for m in y:
            if m in x:
                x.remove(m)
        if list(i) != sorted(list(i)):
            continue
        elif not x:
            continue
        else:
            count += 1
    return count


print(password_count2(245182, 790573))  # 710


def has_double(n):
    num = str(n)
    for i in range(10):
        if str(i)*2 in num:
            return True
    return False


def has_only_double(n):
    num = str(n)
    for i in range(10):
        if str(i)*2 in num and not str(i)*3 in num:
            return True
    return False


total = 0
for x in range(245182, 790573):
    if has_double(x) and list(str(x)) == sorted(list(str(x))):
        total += 1
print(total)


total = 0
for x in range(245182, 790573):
    if has_only_double(x) and list(str(x)) == sorted(list(str(x))):
        total += 1
print(total)
