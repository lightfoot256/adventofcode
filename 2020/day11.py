# Day 10

import copy

def part1(file):
    lines = [list(line.rstrip('\n')) for line in open(file)]

    now = lines.copy()

    h = len(now)
    w = len(now[0])

    # y, x
    ncheck = [
        (-1,-1),
        (-1,0),
        (-1,1),
        (0,-1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    step = 0

    changed = True
    while changed:
        changed = False

        #print("Step:", step)
        #for line in now:
        #    print(line)

        next = copy.deepcopy(now)

        for y in range(0,h):
            for x in range(0,w):

                # Count neighbours
                c = 0
                for n in ncheck:
                    cy = y + n[0]
                    cx = x + n[1]
                    if cy >= 0 and cx >= 0 and cx < w and cy < h:
                        if now[cy][cx] == '#':
                            c+=1

                if now[y][x] == 'L':
                    if c == 0:
                        next[y][x] = '#'
                        changed = True
                if now[y][x] == '#':
                    if c >= 4:
                        next[y][x] = 'L'
                        changed = True

        now = next
        step += 1

    count = 0
    for line in now:
        count += str(line).count('#')

    return count

def part2(file):
    lines = [list(line.rstrip('\n')) for line in open(file)]

    now = lines.copy()

    h = len(now)
    w = len(now[0])

    # y, x
    ncheck = [
        (-1,-1),
        (-1,0),
        (-1,1),
        (0,-1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    step = 0

    changed = True
    while changed:
        changed = False

        #print("Step:", step)
        #for line in now:
        #    print(line)

        next = copy.deepcopy(now)

        for y in range(0,h):
            for x in range(0,w):

                # Count neighbours
                c = 0
                for n in ncheck:

                    for e in range(1, w+h):
                        cy = y + (n[0] * e)
                        cx = x + (n[1] * e)

                        if cy < 0 or cx < 0 or cx >= w or cy >= h:
                            break

                        if now[cy][cx] == 'L':
                            break

                        if now[cy][cx] == '#':
                            c+=1
                            break

                if now[y][x] == 'L':
                    if c == 0:
                        next[y][x] = '#'
                        changed = True
                if now[y][x] == '#':
                    if c >= 5:
                        next[y][x] = 'L'
                        changed = True

        now = next
        step += 1

    count = 0
    for line in now:
        count += str(line).count('#')

    return count

# Run

print("# Part 1")
print("- Test:", part1("day11/example.txt"), 37)
print("- Input:", part1("day11/input.txt"))
print("# Part 2")
print("- Test1:", part2("day11/part2test1.txt"))
print("- Test2:", part2("day11/part2test2.txt"))
print("- Example:", part2("day11/example.txt"), 26)
print("- Input:", part2("day11/input.txt"))
