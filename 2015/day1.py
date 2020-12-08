
from utils import *

DAY = "1"

def part1(input):
    return input.count('(') - input.count(')')

def part2(input):
    floor = 0
    for index, char in enumerate(input):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

        if floor < 0:
            return index + 1

    return -1

validate(part1("(())"), 0)
validate(part1("()()"), 0)
validate(part1("((("), 3)
validate(part1("(()(()("), 3)
validate(part1("))((((("), 3)
validate(part1("())"), -1)
validate(part1("))("), -1)
validate(part1(")))"), -3)
validate(part1(")())())"), -3)

solution("Part 1", DAY, part1)

validate(part2(")"), 1)
validate(part2("()())"), 5)

solution("Part 2", DAY, part2)
