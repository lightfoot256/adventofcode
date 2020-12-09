
# Day 9

def part1(file, preamble):
    lines = [int(line.rstrip('\n')) for line in open(file)]

    for i in range(preamble, len(lines)):
        found = False
        for x in range(i-preamble, i):
            for y in range(i-preamble, i):
                if x == y: continue
                if lines[i] == lines[x]+lines[y]:
                    found = True
        if not found:
            return lines[i]

    return -1


def part2(file, target):
    lines = [int(line.rstrip('\n')) for line in open(file)]

    i = 0
    while i < len(lines):
        c = 0
        j = i

        while c < target and j < len(lines):
            c += lines[j]
            j += 1

        if c == target and j-1 > i:
            cmin = min(lines[i:j])
            cmax = max(lines[i:j])
            return cmin+cmax

        i += 1

    return -1


# Run

print("# Part 1")
print("- Test:", part1("day9/example.txt", 5))
print("- Input:", part1("day9/input.txt", 25))
print("# Part 2")
print("- Test:", part2("day9/example.txt", part1("day9/example.txt", 5)))
print("- Input:", part2("day9/input.txt", part1("day9/input.txt", 25)))
