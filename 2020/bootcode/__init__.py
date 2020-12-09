class BootCode:
    def __init__(self, instructions):
        self.instructions = instructions
        self.accum = 0
        self.idx = 0
        self.ops = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop,
        }
    
    def acc(self, val):
        self.accum += val
        self.idx += 1
    
    def jmp(self, val):
        self.idx += val
    
    def nop(self, val):
        self.idx += 1

    def reset(self):
        self.idx = 0
        self.accum = 0

    def step(self):
        op, val = self.instructions[self.idx]
        self.ops[op](val)

    def repair(self):
        swap = {'jmp': 'nop', 'nop': 'jmp'}
        cycles = list(self.run()[1])
        while cycles:
            cur = cycles.pop()
            op, val = self.instructions[cur]
            if op in ('jmp', 'nop'):
                self.instructions[cur] = [swap[op], val]
            res, cycle = self.run()
            if not cycle:
                return res
            self.instructions[cur] = [op, val]
    
    def run(self):
        self.reset()
        cycles = set()
        while True:
            if self.idx == len(self.instructions):
                return self.accum, None
            if self.idx in cycles:
                return self.accum, cycles
            cycles.add(self.idx)
            self.step()
