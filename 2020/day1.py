
def part1(file):
    lines = [line.rstrip('\n') for line in open(file)]
    for a in lines:
        for b in lines:
            if int(a) + int(b) == 2020:
                return int(a) * int(b)

    input.close()

def part2(file):
    lines = [int(line.rstrip('\n')) for line in open(file)]
    for a in lines:
        for b in lines:
            for c in lines:
                if a+b+c == 2020:
                    return a * b * c

    input.close()

print("Part 1")
print("Test:", part1("Day1/test.txt"))
print("Input:", part1("Day1/input.txt"))

print("Part 2")
print("Test Answer:", part2("Day1/test.txt"))
print("Input Answer:", part2("Day1/input.txt"))
