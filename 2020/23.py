inp = 925176834

class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None


def part_one(inp):
    inp = list(map(int, str(inp)))

    nodes = {}
    prev = None

    for x in inp:
        cur = Node(x)
        if prev:
            prev.nxt = cur
        prev = cur
        nodes[x] = cur

    head = nodes[inp[0]]
    prev.nxt = head

    cur = head
    for _ in range(100):
        val = cur.val
        a = cur.nxt
        b = a.nxt
        c = b.nxt
        cur.nxt = c.nxt
        dest = val-1 if val!=1 else 9
        while dest in (a.val, b.val, c.val):
            dest -= 1
            if dest == 0: dest = 9
        dest_node = nodes[dest]
        c.nxt = dest_node.nxt
        dest_node.nxt = a
        cur = cur.nxt
    
    while cur.val != 1:
        cur = cur.nxt

    res = []
    cur = cur.nxt
    while cur.val != 1:
        res.append(str(cur.val))
        cur = cur.nxt
    return ''.join(res)



def part_two(inp):
    inp = list(map(int, str(inp)))

    nodes = {}
    prev = None

    for x in inp:
        cur = Node(x)
        if prev:
            prev.nxt = cur
        prev = cur
        nodes[x] = cur
    
    for x in range(10, 1000001):
        cur = Node(x)
        prev.nxt = cur
        prev = cur
        nodes[x] = cur

    head = nodes[inp[0]]
    prev.nxt = head

    cur = head
    for _ in range(10000000):
        val = cur.val
        a = cur.nxt
        b = a.nxt
        c = b.nxt
        cur.nxt = c.nxt
        dest = val-1 if val!=1 else 1000000
        while dest in (a.val, b.val, c.val):
            dest -= 1
            if dest == 0: dest = 1000000
        dest_node = nodes[dest]
        c.nxt = dest_node.nxt
        dest_node.nxt = a
        cur = cur.nxt

    while cur.val != 1:
        cur = cur.nxt
    
    return cur.nxt.val * cur.nxt.nxt.val


print(f'Part 1: {part_one(inp)}')  # 69852437
print(f'Part 2: {part_two(inp)}')  # 91408386135
