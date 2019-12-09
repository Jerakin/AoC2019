from pathlib import Path


def calculate_fuel(mass: int):
    return int(mass / 3) - 2


def total_fuel(module_mass: int):
    part_fuel = calculate_fuel(module_mass)
    _total_fuel = part_fuel
    fuel = part_fuel
    while fuel > 0:
        fuel = max(calculate_fuel(fuel), 0)
        _total_fuel += fuel
    return _total_fuel


def part1():
    total = 0
    with open(Path(__file__).parent / "day1.txt", "r") as f:
        for line in f.readlines():
            total = calculate_fuel(int(line))
    return total


def part2():
    total = 0
    with open(Path(__file__).parent / "day1.txt", "r") as f:
        for line in f.readlines():
            total += total_fuel(int(line))
    return total


def test():
    assert calculate_fuel(12) == 2
    assert calculate_fuel(14) == 2
    assert calculate_fuel(1969) == 654
    assert calculate_fuel(100756) == 33583
    assert calculate_fuel(100756) == 33583

    assert total_fuel(14) == 2
    assert total_fuel(1969) == 966
    assert total_fuel(100756) == 50346


print(part2())
