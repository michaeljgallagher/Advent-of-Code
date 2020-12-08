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
    
    def acc(self, val):
        self.accum += val
        self.idx += 1
    
    def jmp(self, val):
        self.idx += val
    
    def nop(self, val):
        self.idx += 1
    
    def step(self):
        op, val = self.instructions[self.idx]
        self.ops[op](val)
    
    def run(self):
        while True:
            if self.idx in self.seen:
                break
            self.seen.add(self.idx)
            self.step()
