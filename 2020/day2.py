
import re

def part1(file):
    p = re.compile("([0-9]*)-([0-9]*) ([a-zA-Z]): (.*)")
    lines = [line.rstrip('\n') for line in open(file)]
    valid = 0
    for line in lines:
        m = p.match(line)

        min = int(m.group(1))
        max = int(m.group(2))
        char = m.group(3)
        test = m.group(4)

        count = test.count(char)

        if min <= count <= max:
            valid = valid + 1

    return valid

def part2(file):
    p = re.compile("([0-9]*)-([0-9]*) ([a-zA-Z]): (.*)")
    lines = [line.rstrip('\n') for line in open(file)]
    valid = 0
    for line in lines:
        m = p.match(line)

        min = int(m.group(1))
        max = int(m.group(2))
        char = m.group(3)
        test = m.group(4)

        #print(min, max, char, test, test[min-1], test[max-1])

        a = test[min-1] == char
        b = test[max-1] == char

        if( a != b ):
            valid = valid + 1

    return valid

print("Part 1")
print("Test:", part1("Day2/example.txt"))
print("Input:", part1("Day2/input.txt"))

print("Part 2")
print("Test Answer:", part2("Day2/example.txt"))
print("Input Answer:", part2("Day2/input.txt"))
