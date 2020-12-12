# Day 12

import png

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


def part2_animation(prefix, file):
    lines = [line.rstrip('\n') for line in open(file)]

    l,u,r,d = 0,0,0,0

    wx, wy = 10, 1
    sx, sy, sh = 0, 0, 0

    maxsteps = 0

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

        print("P", sx, sy, wx, wy)

        l = min(l, sx+wx, sx)
        u = max(u, sy+wy, sy)

        r = max(r, sx+wx, sx)
        d = min(d, sy+wy, sy)

        maxsteps += 1

    print("Initial run...", maxsteps)

    w = r-l+1
    h = u-d+1

    step = 0

    print("LURD:", l,u,r,d)

    print("DIMS:", w,h)

    #w = 3
    #h = 2

    w //= 64
    h //= 64

    w += 1
    h += 1

    img = []
    for y in range(h):
        img.append([0]*w)

    #img = [[0]*w]*h

    print("Generated base image...")

    wx, wy = 10, 1
    sx, sy, sh = 0, 0, 0

    palette = [(0, 0, 0), (255, 255, 255), (255, 0, 0)]

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

                img[(sy-d)//64][(sx-l)//64] = 1
                img[(sy-d+wy)//64][(sx-l+wx)//64] = 2

        img[(sy-d)//64][(sx-l)//64] = 1
        img[(sy-d+wy)//64][(sx-l+wx)//64] = 2

        with open("day12/step-" + prefix + "-" + str(step) + ".png", 'wb') as f:
            writer = png.Writer(w, h, palette=palette, bitdepth=2)
            writer.write(f, img)

        print("Step", step)

        step += 1


    return -1



# Run

part2_animation("eg", "day12/example.txt")
part2_animation("in", "day12/input.txt")
