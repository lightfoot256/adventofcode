# Day 14

EMPTY = 0
OCCUPIED = 1

DEBUG = {
    EMPTY: '.',
    OCCUPIED: '#'
}

def debug(cube):

    print(cube)

    minx, maxx = 0, 0
    miny, maxy = 0, 0
    minz, maxz = 0, 0

    for c in cube:
        minx = min(minx, c[0])
        maxx = max(maxx, c[0])

        miny = min(miny, c[1])
        maxy = max(maxy, c[1])

        minz = min(minz, c[2])
        maxz = max(maxz, c[2])

    print("x:", minx, "..", maxx, "y:", miny, "..", maxy, "z:", minz, "..", maxz)

    for z in range(minz, maxz+1):
        print("z=", z)
        for y in range(miny, maxy+1):
            for x in range(minx, maxx+1):
                print(DEBUG[cube.get((x, y, z), 0)], end='')
            print()


def part1(file):
    lines = [line.rstrip('\n') for line in open(file)]

    cube = {}

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                cube[(x, y, 0)] = OCCUPIED

    next = {}

    for i in range(6):

        #print("Cycle", i)

        inactive_to_check = []

        #debug(cube)

        for c in cube:

            if cube[c] == OCCUPIED:

                count = 0
                for dz in range(-1, 2):
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            # Skip center
                            if dx == 0 and dy == 0 and dz == 0:
                                continue

                            cx = dx + c[0]
                            cy = dy + c[1]
                            cz = dz + c[2]

                            if cube.get((cx, cy, cz), 0) == EMPTY:
                                inactive_to_check.append((cx, cy, cz))

                            if cube.get((cx, cy, cz), 0) == OCCUPIED:
                                count += 1

                if count == 2 or count == 3:
                    # stay active; i.e. copy
                    next[c] = OCCUPIED

        for c in inactive_to_check:

            count = 0
            for dz in range(-1, 2):
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        # Skip center
                        if dx == 0 and dy == 0 and dz == 0:
                            continue

                        cx = dx + c[0]
                        cy = dy + c[1]
                        cz = dz + c[2]

                        if cube.get((cx, cy, cz), 0) == OCCUPIED:
                            count += 1

            if count == 3:
                next[c] = OCCUPIED

        cube = next
        next = {}

    return sum(cube.values())


def part2(file):
    lines = [line.rstrip('\n') for line in open(file)]

    cube = {}

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                cube[(x,y,0,0)] = OCCUPIED

    next = {}

    for i in range(6):

        inactive_to_check = []

        for c in cube:
            if cube[c] == OCCUPIED:

                count = 0
                for dw in range(-1, 2):
                    for dz in range(-1, 2):
                        for dy in range(-1, 2):
                            for dx in range(-1, 2):
                                # Skip center
                                if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                                    continue

                                cx = dx + c[0]
                                cy = dy + c[1]
                                cz = dz + c[2]
                                cw = dw + c[3]

                                if cube.get((cx, cy, cz, cw), 0) == EMPTY:
                                    inactive_to_check.append((cx, cy, cz, cw))

                                if cube.get((cx, cy, cz, cw), 0) == OCCUPIED:
                                    count += 1

                if count == 2 or count == 3:
                    # stay active; i.e. copy
                    next[c] = OCCUPIED

        for c in inactive_to_check:

            count = 0
            for dw in range(-1, 2):
                for dz in range(-1, 2):
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            # Skip center
                            if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                                continue

                            cx = dx + c[0]
                            cy = dy + c[1]
                            cz = dz + c[2]
                            cw = dw + c[3]

                            if cube.get((cx, cy, cz, cw), 0) == OCCUPIED:
                                count += 1

            if count == 3:
                # become active
                next[c] = 1

        cube = next
        next = {}

    return sum(cube.values())

# Run

print("# Part 1")
print("- Test:", part1("day17/example.txt"), 112)
print("- Input:", part1("day17/input.txt"), 5902420735773)

print("# Part 2")
print("- Example:", part2("day17/example.txt"), 848)
print("- Input:", part2("day17/input.txt"), 1624)
