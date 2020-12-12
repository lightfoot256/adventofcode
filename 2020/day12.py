# Day 12


def part1(file):
    lines = [line.rstrip('\n') for line in open(file)]

    x, y, h = 0, 0, 0

    for line in lines:
        op = line[0]
        amount = int(line[1:])

        if op == 'N':
            y += amount
        if op == 'S':
            y -= amount
        if op == 'E':
            x += amount
        if op == 'W':
            x -= amount

        if op == 'L':
            h = (h + amount) % 360
        if op == 'R':
            h = (h - amount) % 360

        if op == 'F':
            if h == 0:
                x += amount
            if h == 90:
                y += amount
            if h == 180:
                x -= amount
            if h == 270:
                y -= amount

    return abs(x) + abs(y)


def rotate_left(sh, by, wx, wy):
    if by == 90:
        wx, wy = (-wy, wx)
    if by == 180:
        wx, wy = (-wy, wx)
        wx, wy = (-wy, wx)
    if by == 270:
        wx, wy = (-wy, wx)
        wx, wy = (-wy, wx)
        wx, wy = (-wy, wx)

    sh = (sh + by) % 360

    return wx, wy, sh


def rotate_right(sh, by, wx, wy):
    if by == 90:
        wx, wy = (wy, -wx)
    if by == 180:
        wx, wy = (wy, -wx)
        wx, wy = (wy, -wx)
    if by == 270:
        wx, wy = (wy, -wx)
        wx, wy = (wy, -wx)
        wx, wy = (wy, -wx)

    sh = (sh - by) % 360

    return wx, wy, sh


def part2(file):
    lines = [line.rstrip('\n') for line in open(file)]

    wx, wy = 10, 1
    sx, sy, sh = 0, 0, 0

    for line in lines:
        op = line[0]
        amount = int(line[1:])

        if op == 'N':
            wy += amount
        if op == 'S':
            wy -= amount
        if op == 'E':
            wx += amount
        if op == 'W':
            wx -= amount

        if op == 'L':
            wx, wy, sh = rotate_left(sh, amount, wx, wy)
        if op == 'R':
            wx, wy, sh = rotate_right(sh, amount, wx, wy)

        # move TO the ship; not TOwards it
        if op == 'F':
            for n in range(0, amount):
                sx, sy = (sx + wx, sy + wy)

    return abs(sx) + abs(sy)


# Run

print("# Part 1")
print("- Test:", part1("day12/example.txt"), 25)
print("- Input:", part1("day12/input.txt"), 1319)
print("# Part 2")
print("- Test1:", part2("day12/example.txt"), 286)
print("- Input:", part2("day12/input.txt"), 62434)
