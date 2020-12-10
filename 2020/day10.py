# Day 10

def search(lines, i, path, total):
    nlines = lines[:]
    if (i >= 0):
        del nlines[i]

    if (len(nlines) == 0):
        if (path[-1] + 3 == total):
            return path
        return None

    for i in range(0, len(nlines)):
        npath = path[:]
        if (1 <= nlines[i] - npath[-1] <= 3):
            npath.append(nlines[i])
            s = search(nlines, i, npath, total)
            if s:
                return s

    return None


def part1(file):
    lines = [int(line.rstrip('\n')) for line in open(file)]

    lines.sort()

    total = max(lines) + 3

    r = search(lines, -1, [0], total)
    r.append(total)

    d = [r[i + 1] - r[i] for i in range(len(r) - 1)]

    print("final path:")
    print(r)
    print(d)

    c1 = d.count(1)
    c3 = d.count(3)

    print(c1, c3)

    return c1 * c3


def part2(file):
    q = [int(line.rstrip('\n')) for line in open(file)]

    total = max(q) + 3
    q.sort()
    q.insert(0, 0)
    q.append(total)

    # Get differences
    d = [q[i + 1] - q[i] for i in range(len(q) - 1)]

    # Convert to string
    ds = ''.join([str(i) for i in d])

    # Split on '3' to get groups of '1' avoid list comprehension and zip and slicing :D
    valid = 1
    for r in ds.split('3'):
        # if len(r) == 1:  valid *= 1 + 0
        # if len(r) == 2:  valid *= 1 + 1
        # if len(r) == 3:  valid *= 2 + 2
        # if len(r) == 4:  valid *= 4 + 3

        if len(r) <= 1:
            valid *= 1
        elif len(r) == 2:
            valid *= 2
        else:
            valid *= pow(2, len(r)-2) + (len(r) - 1)

    return valid


# Run

print("# Part 1")
print("- Test:", part1("day10/example.txt"))
print("- Test:", part1("day10/example2.txt"))
print("- Input:", part1("day10/input.txt"))
print("# Part 2")
print("- Test:", part2("day10/example.txt"), 8)
print("- Test:", part2("day10/example2.txt"), 19208)
print("- Input:", part2("day10/input.txt"), 10578455953408)
