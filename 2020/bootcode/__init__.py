from collections import Counter


class BootCode:
    def __init__(self, instructions):
        self.instructions = instructions
        self.accum = 0
        self.idx = 0
        #self.seen = set()
        self.ops = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop,
        }
        #self.halt = False
        self.length = len(self.instructions)
    
    def acc(self, val):
        self.accum += val
        self.idx += 1
    
    def jmp(self, val):
        self.idx += val
    
    def nop(self, val):
        self.idx += 1

    def cycle_check(self):
        if self.idx in self.seen:
            self.halt = True

    def reset(self):
        self.idx = 0
        self.accum = 0


    def repair(self):
        instructions = self.instructions
        swap = {'jmp': 'nop', 'nop': 'jmp'}
        cycles = list(self.run()[1])
        while cycles:
            cur = cycles.pop()
            op, val = instructions[cur]
            if op in ('jmp', 'nop'):
                instructions[cur] = [swap[op], val]
            res, cycle = self.run()
            if not cycle:
                return res
            instructions[cur] = [op, val]



    
    def step(self):
        op, val = self.instructions[self.idx]
        #self.seen.add(self.idx)
        self.ops[op](val)
        #self.cycle_check()
    
    def run(self):
        """ while not self.halt and self.idx < self.length:
            self.step() """
        self.reset()
        instructions = self.instructions
        cycles = set()
        while True:
            if self.idx == self.length:
                return self.accum, None
            if self.idx in cycles:
                return self.accum, cycles
            cycles.add(self.idx)
            self.step()