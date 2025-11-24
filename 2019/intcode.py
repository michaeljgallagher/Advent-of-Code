from collections import defaultdict, deque
from typing import Callable, List, Optional


class Intcode:
    def __init__(self, program: List[int]):
        self.ops = {
            1: self.op_add,
            2: self.op_multiply,
            3: self.op_input,
            4: self.op_output,
            5: self.op_jump_if_true,
            6: self.op_jump_if_false,
            7: self.op_less_than,
            8: self.op_equals,
            9: self.op_adjust_relative_base,
            99: self.op_halt,
        }
        self.reset(program)

    def reset(self, program: List[int]):
        self.memory = defaultdict(int)
        for i, val in enumerate(program):
            self.memory[i] = val
        self.pointer = 0
        self.relative_base = 0
        self.halted = False
        self.input_queue = deque()
        self.output_queue = deque()

    def get_param(self, offset: int, mode: int) -> int:
        v = self.memory[self.pointer + offset]
        if mode == 0:  # position mode
            return self.memory[v]
        elif mode == 1:  # immediate mode
            return v
        elif mode == 2:  # relative mode
            return self.memory[self.relative_base + v]
        else:
            raise ValueError(f"Unknown parameter mode: {mode}")

    def get_address(self, offset: int, mode: int) -> int:
        v = self.memory[self.pointer + offset]
        if mode == 0:  # position mode
            return v
        elif mode == 2:  # relative mode
            return self.relative_base + v
        else:
            raise ValueError(f"Invalid mode for address: {mode}")

    def parse_instruction(self, inst: int) -> tuple:
        opcode = inst % 100
        mode1 = (inst // 100) % 10
        mode2 = (inst // 1000) % 10
        mode3 = (inst // 10000) % 10
        return opcode, mode1, mode2, mode3

    def add_input(self, x: int):
        self.input_queue.append(x)

    def add_inputs(self, vals: List[int]):
        self.input_queue.extend(vals)

    def get_output(self) -> Optional[int]:
        return self.output_queue.popleft() if self.output_queue else None

    def get_all_outputs(self) -> List[int]:
        outputs = self.output_queue[:]
        self.output_queue = deque()
        return outputs

    def op_add(self, mode1: int, mode2: int, mode3: int) -> bool:
        p1 = self.get_param(1, mode1)
        p2 = self.get_param(2, mode2)
        addr = self.get_address(3, mode3)
        self.memory[addr] = p1 + p2
        self.pointer += 4
        return True

    def op_multiply(self, mode1: int, mode2: int, mode3: int) -> bool:
        p1 = self.get_param(1, mode1)
        p2 = self.get_param(2, mode2)
        addr = self.get_address(3, mode3)
        self.memory[addr] = p1 * p2
        self.pointer += 4
        return True

    def op_input(self, mode1: int, mode2: int, mode3: int) -> bool:
        if not self.input_queue:
            return False
        addr = self.get_address(1, mode1)
        self.memory[addr] = self.input_queue.popleft()
        self.pointer += 2
        return True

    def op_output(self, mode1: int, mode2: int, mode3: int) -> bool:
        value = self.get_param(1, mode1)
        self.output_queue.append(value)
        if self.output_callback:
            self.output_callback(value)
        self.pointer += 2
        return not self.pause_on_output

    def op_jump_if_true(self, mode1: int, mode2: int, mode3: int) -> bool:
        p1 = self.get_param(1, mode1)
        p2 = self.get_param(2, mode2)
        if p1 != 0:
            self.pointer = p2
        else:
            self.pointer += 3
        return True

    def op_jump_if_false(self, mode1: int, mode2: int, mode3: int) -> bool:
        p1 = self.get_param(1, mode1)
        p2 = self.get_param(2, mode2)
        if p1 == 0:
            self.pointer = p2
        else:
            self.pointer += 3
        return True

    def op_less_than(self, mode1: int, mode2: int, mode3: int) -> bool:
        p1 = self.get_param(1, mode1)
        p2 = self.get_param(2, mode2)
        addr = self.get_address(3, mode3)
        self.memory[addr] = 1 if p1 < p2 else 0
        self.pointer += 4
        return True

    def op_equals(self, mode1: int, mode2: int, mode3: int) -> bool:
        p1 = self.get_param(1, mode1)
        p2 = self.get_param(2, mode2)
        addr = self.get_address(3, mode3)
        self.memory[addr] = 1 if p1 == p2 else 0
        self.pointer += 4
        return True

    def op_adjust_relative_base(self, mode1: int, mode2: int, mode3: int) -> bool:
        p1 = self.get_param(1, mode1)
        self.relative_base += p1
        self.pointer += 2
        return True

    def op_halt(self, mode1: int, mode2: int, mode3: int) -> bool:
        self.halted = True
        return False

    def run(
        self,
        inputs: Optional[List[int]] = None,
        pause_on_output: bool = False,
        output_callback: Optional[Callable[[int], None]] = None,
    ) -> List[int]:
        if inputs:
            self.add_inputs(inputs)
        self.pause_on_output = pause_on_output
        self.output_callback = output_callback
        while not self.halted:
            instruction = self.memory[self.pointer]
            opcode, mode1, mode2, mode3 = self.parse_instruction(instruction)
            if opcode not in self.ops:
                raise ValueError(f"Unknown opcode: {opcode} at position {self.pointer}")
            if not self.ops[opcode](mode1, mode2, mode3):
                break
        return self.output_queue

    def run_until_halt(self, inputs: Optional[List[int]] = None) -> List[int]:
        return self.run(inputs=inputs, pause_on_output=False)

    def copy(self):
        new_comp = Intcode([])
        new_comp.memory = self.memory.copy()
        new_comp.pointer = self.pointer
        new_comp.relative_base = self.relative_base
        new_comp.halted = self.halted
        new_comp.input_queue = self.input_queue[:]
        new_comp.output_queue = self.output_queue[:]
        return new_comp
