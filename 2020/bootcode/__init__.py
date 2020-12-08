class BootCode:
    def __init__(self, instructions):
        self.instructions = instructions
        self.accum = 0
        self.idx = 0
        self.seen = set()
        self.ops = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop,
        }
        self.halt = False
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
    
    def step(self):
        op, val = self.instructions[self.idx]
        self.seen.add(self.idx)
        self.ops[op](val)
        self.cycle_check()
    
    def run(self):
        while not self.halt and self.idx < self.length:
            self.step()
