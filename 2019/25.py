from intcode import Intcode


def parse_input():
    with open("25.txt", "r") as file:
        data = file.read()
    return list(map(int, data.split(",")))


# - mutex
# - asterisk
# - space law space brochure
# - food ration

program = parse_input()
computer = Intcode(program)
while True:
    computer.run()
    print("".join(map(chr, computer.output_queue)))
    inp = input("input: ")
    computer.add_inputs(list(map(ord, inp + "\n")))
