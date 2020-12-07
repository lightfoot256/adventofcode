
import re

def part1(file, vector):
    p = re.compile("([0-9]*)-([0-9]*) ([a-zA-Z]): (.*)")
    lines = [line.rstrip('\n') for line in open(file)]
    valid = 0

    stride = len(lines[0])
    location = (0, 0)

    while location[1] < len(lines):
        line = lines[location[1]]
        if line[location[0] % stride] == '#':
            valid = valid + 1

        #print(location, line, valid, line[location[0] % stride])

        location = (location[0] + vector[0], location[1] + vector[1])

    return valid

def part2(file):
    a = part1(file, (1,1))
    b = part1(file, (3,1))
    c = part1(file, (5,1))
    d = part1(file, (7,1))
    e = part1(file, (1,2))

    print(a,b,c,d,e)

    return a*b*c*d*e


print("Part 1")
print("Test:", part1("Day3/example.txt", (3, 1)), "Expected", 7)
print("Input:", part1("Day3/input.txt", (3, 1)))

print("Part 2")
print("Test Answer:", part2("Day3/example.txt"))
print("Input Answer:", part2("Day3/input.txt"))
