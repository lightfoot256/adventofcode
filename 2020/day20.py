# Day 19

import re

ROTATE = [0, 90, 180, 270]


def perform_hflip(data):

    result = []
    for y in range(0,10):
        result.append(['.']*10)
        for x in range(0,10):
            result[y][x] = data[y][9-x]
    return result


def perform_vflip(data):
    result = []
    for y in range(0,10):
        result.append(['.']*10)
        for x in range(0,10):
            result[y][x] = data[9-y][x]
    return result


def perform_rotate_90(data):
    result = []
    for y in range(0, 10):
        result.append(['.'] * 10)
        for x in range(0, 10):
            result[y][x] = data[9 - x][y]
    return result


def perform_rotate(data, r):

    if r == 0:
        return data[:]
    if r == 90:
        return perform_rotate_90(data)
    if r == 180:
        tmp = perform_rotate_90(data)
        return perform_rotate_90(tmp)
    if r == 270:
        tmp = perform_rotate_90(data)
        tmp = perform_rotate_90(tmp)
        return perform_rotate_90(tmp)


def variate_tile(data):

    variations = {}

    for hflip in range(0,2):
        for vflip in range(0,2):
            for rotate in range(0,4):

                name = []

                varied = data[:]
                if hflip == 1:
                    varied = perform_hflip(varied)
                    name.append('hflip')
                if vflip == 1:
                    varied = perform_vflip(varied)
                    name.append('vflip')
                varied = perform_rotate(varied, ROTATE[rotate])
                name.append('rotate-' + str(ROTATE[rotate]))

                name = ', '.join(name)

                variations[name] = varied

    return variations


# Convert bit-string to number
def convert_to_number(row):
    num = 0
    for i in range(0, 10):
        if row[9-i] == '#':
            num |= 1 << i

    return num


def parse_tile(data):

    t = []
    b = []
    l = []
    r = []

    for x in range(0,10):
        t.append(data[0][x])
        b.append(data[9][9-x])

    for y in range(0,10):
        l.append(data[y][0])
        r.append(data[9-y][9])

    return {
        "data": data,
        "edges": [
            convert_to_number(t),
            convert_to_number(r),
            convert_to_number(b),
            convert_to_number(l),
        ]
    }


def load_tile(data):
    variations = variate_tile(data)
    result = {}
    for var in variations:
        result[var] = parse_tile(variations[var])
    return result


def part1(file):
    tiles_string = open(file, 'r').read().split('\n\n')

    tiles = {}

    for tile in tiles_string:
        lines = tile.split('\n')
        l1 = lines[0].split(' ')
        print(l1)
        number = l1[1].split(':')[0]
        tiles[number] = load_tile(lines[1:])

    for tile in tiles:

        print('Tile: ', tile)

        for var in tiles[tile]:
            print(' -', var)

            for d in tiles[tile][var]['data']:
                print('  : ', d)

            print('---')

            for e in tiles[tile][var]['edges']:
                print('  * ', e)


    # find the corners
    # find the 4 tiles which have 2 sides that dont match any other side?

    corners = {}
    edges = {}
    middle = {}

    for tile in tiles:
        for var in tiles[tile]:

            matchedEdges = 0
            for e in tiles[tile][var]['edges']:
                for tilej in tiles:
                    if tilej==tile:
                        continue
                    for varj in tiles[tilej]:
                        for ej in tiles[tilej][varj]['edges']:

                            if e == ej:
                                matchedEdges += 1

            #print('- matchedEdges', matchedEdges)

            if matchedEdges == 16:
                corners[tile] = 1
            if matchedEdges == 24:
                edges[tile] = 1
            if matchedEdges == 32:
                middle[tile] = 1

    print(corners)
    print(edges)
    print(middle)

    result = 1
    for c in corners:
        result *= int(c)

    return result


def part2(file):
    return 0

# Run


# print("# Part 1")
# print("- Example:", part1("day20/example.txt"), 20899048083289)
# print("- Input:", part1("day20/input.txt"), 18482479935793)

print("# Part 2")
print("- Example:", part1("day20/example.txt"), 12)
#print("- Input:", part2("day20/input.txt"), 323)
