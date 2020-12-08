import re

def seatId(row,column):
    return row*8 + column

def decode(seat):

    f = int(0)
    b = int(127)
    l = int(0)
    r = int(7)

    for c in seat:
        #print(c)
        #print(f, b, l, r)

        if c == "F":
            b = f+(b-f)//2
        if c == "B":
            f = f+(b-f)//2 + 1
        if c == "L":
            r = l+(r-l)//2
        if c == "R":
            l = l+(r-l)//2 + 1

        #print(" -> ", f, b, l, r)

    return f, l

def part1(filename):
    lines = [line.rstrip('\n') for line in open(filename)]

    ids = []

    for line in lines:
        seat = decode(line)
        id = seatId(*seat)
        ids.append(id)

    return max(ids)


def part2(filename):
    lines = [line.rstrip('\n') for line in open(filename)]

    map = [['.' for i in range(128)] for j in range(8)]


    available_seats = []
    for i in range(128):
        for j in range(8):
            available_seats.append((i, j))

    print(available_seats)

    ids = []

    minrow = 128
    maxrow = 0

    for line in lines:
        seat = decode(line)
        id = seatId(*seat)

        if seat[0] < minrow:
            minrow = seat[0]
        if seat[0] > maxrow:
            maxrow = seat[0]

        available_seats.remove(seat)

        map[seat[1]][seat[0]] = '#'


    for y, m in enumerate(map):
        print(y, ''.join(m))

    print(minrow, maxrow)

    for remaining in available_seats:
        if(minrow < remaining[0] < maxrow):
            print("Your seat:", remaining)
            print("Your id:", seatId(*remaining))

    #print(available_seats)

    return valid

def valid(given, expected):
    print(given, expected, given == expected)

    if(given != expected):
        print("  ^ Failed!")


valid(decode("FBFBBFFRLR"), (44, 5))
valid(seatId(44, 5), 357)

valid(decode("BFFFBBFRRR"), (70, 7))
valid(seatId(70, 7), 567)
valid(decode("FFFBBBFRRR"), (14, 7))
valid(seatId(14, 7), 119)
valid(decode("BBFFBBFRLL"), (102, 4))
valid(seatId(102, 4), 820)


print("Part 1")
print("Input:", part1("day5/input.txt"))

print("Part 2")
print("Input:", part2("day5/input.txt"))
