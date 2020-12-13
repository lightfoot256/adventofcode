# Day 13


def part1(file):
    lines = [line.rstrip('\n') for line in open(file)]

    nearest = int(lines[0])
    ids = [int(id) for id in lines[1].split(',') if id.isdigit()]

    print(nearest)
    print(ids)

    i = nearest
    next = None
    bus = None
    while bus is None:

        for id in ids:
            if i % id == 0:
                next = i
                bus = id
                print(i, id)
                break

        i += 1

    return (next - nearest) * bus


def part2(file):
    lines = [line.rstrip('\n') for line in open(file)]

    ids = [(i, int(id)) for i, id in enumerate(lines[1].split(',')) if id != 'x']

    step, time = 1, 0
    for i, id in ids:

        #print("#", i, id, step)

        while True:
            #print(" - ", step, time, i, id)

            if (i+time) % id == 0:
                break

            time += step

        step *= id

    return time

# Run

print("# Part 1")
print("- Test:", part1("day13/example.txt"), 295)
print("- Input:", part1("day13/input.txt"), 1319)

print("# Part 2")
print("- Example:", part2("day13/example.txt"), 1068781)

print("- Test1:", part2("day13/test1.txt"), 3417)
print("- Test2:", part2("day13/test2.txt"), 754018)
print("- Test3:", part2("day13/test3.txt"), 779210)
print("- Test4:", part2("day13/test4.txt"), 1261476)
print("- Test5:", part2("day13/test5.txt"), 1202161486)

print("- Input:", part2("day13/input.txt"), 62434)
