from collections import deque


class Intcode:
    def __init__(self, intcode):
        self.intcode = intcode
        self.copy = self.intcode.copy()
        self.index = 0

        self.modes = {'0': lambda x: self.read(x),  # position mode
                      '1': lambda x: x}             # immediate mode

        self.opcodes = {'01': lambda x, y, out: self.write(x + y, out),
                        '02': lambda x, y, out: self.write(x * y, out),
                        '03': lambda x: self.write(int(input('System ID: ')), x),
                        '04': lambda x: print('Diagnostic Code: {}'.format(x)),
                        '05': lambda x, y: self.jump(index=y) if x else None,
                        '06': lambda x, y: self.jump(index=y) if not x else None,
                        '07': lambda x, y, out: self.write(int(x < y), out),
                        '08': lambda x, y, out: self.write(int(x == y), out),
                        '99': None}

        self.inputs = deque()
        self.output = deque()

    def read(self, index=None):
        if index is None:
            index = self.index
            self.index += 1
        return self.copy[index]

    def jump(self, index):
        self.index = index

    def write(self, value, index=None):
        if index is None:
            index = self.index
        self.copy[index] = value

    def padding(self, s, opcode):
        param_counts = {'01': 3,
                        '02': 3,
                        '03': 1,
                        '04': 1,
                        '05': 2,
                        '06': 2,
                        '07': 3,
                        '08': 3}
        num_params = param_counts[opcode]

        if opcode in ['04', '05', '06']:
            return s.zfill(num_params)
        return '1' + s.zfill(num_params-1)

    def run(self, inputs=None):
        self.index = 0
        self.copy = self.intcode.copy()

        if inputs:
            self.opcodes['03'] = lambda x: self.write(int(self.inputs.pop()), x)
            self.opcodes['04'] = lambda x: self.output.appendleft(x)
            for q in inputs:
                self.inputs.appendleft(q)

        while True:
            raw = str(self.read())
            opcode = raw[-2:].zfill(2)
            instruction = self.opcodes[opcode]
            if instruction is None:
                break
            else:
                modes = reversed(self.padding(raw[:-2], opcode))
                params = (self.modes[mode](self.read()) for mode in modes)
                instruction(*params)
        return self.index
