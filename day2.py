from pathlib import Path


class Day2:
    def __init__(self, program_str):
        self.program_switch = {
            1: {"program": self.add},
            2: {"program": self.multiply},
            99: {"program": self.stop}
        }
        self.opt_code = list([int(x) for x in program_str.split(",")])
        self.position = 0

    def stop(self):
        raise StopIteration

    def multiply(self):
        pos_1 = self.opt_code[self.position + 1]
        pos_2 = self.opt_code[self.position + 2]
        pos_3 = self.opt_code[self.position + 3]
        self.opt_code[pos_3] = self.opt_code[pos_1] * self.opt_code[pos_2]
        self.position += 4

    def add(self):
        pos_1 = self.opt_code[self.position + 1]
        pos_2 = self.opt_code[self.position + 2]
        pos_3 = self.opt_code[self.position + 3]
        self.opt_code[pos_3] = self.opt_code[pos_1] + self.opt_code[pos_2]
        self.position += 4

    def calibrate(self, pos, value):
        self.opt_code[pos] = value

    def run(self):
        try:
            while True:
                program = self.program_switch[self.opt_code[self.position]]
                program["program"]()
        except StopIteration:
            pass

    @property
    def value(self):
        return self.opt_code[0]

    def __repl__(self):
        return ",".join([str(x) for x in self.opt_code])

    def __str__(self):
        return ",".join([str(x) for x in self.opt_code])

    def __getitem__(self, index):
        return self.opt_code[index]


def part1():
    with open(Path(__file__).parent / "day2.txt", "r") as f:
        input_program = f.read()
    p = Day2(input_program)
    p.calibrate(1, 12)
    p.calibrate(2, 2)
    p.run()
    return p.value


def part2():
    for noun in range(100):
        for verb in range(100):
            with open(Path(__file__).parent / "day2.txt", "r") as f:
                input_program = f.read()
            p = Day2(input_program)
            p.calibrate(1, noun)
            p.calibrate(2, verb)
            p.run()
            if p.value == 19690720:
                return p[1], p[2]


def run(program_str: str):
    p = Day2(program_str)
    p.run()
    return str(p)


def test():
    assert run("1,9,10,3,2,3,11,0,99,30,40,50") == "3500,9,10,70,2,3,11,0,99,30,40,50"
    assert run("1,0,0,0,99") == "2,0,0,0,99"
    assert run("2,3,0,3,99") == "2,3,0,6,99"
    assert run("2,4,4,5,99,0") == "2,4,4,5,99,9801"
    assert run("1,1,1,4,99,5,6,0,99") == "30,1,1,4,2,5,6,0,99"


print(part2())
