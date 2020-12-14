# Day 14

import re


def part1(file):
    lines = [line.rstrip('\n') for line in open(file)]

    re1 = re.compile("^mask = (.*)$")
    re2 = re.compile("^mem\[(.*)\] = (.*)$")

    mask_op = 0
    mask_mask = 0

    mem = {}

    for line in lines:
        m1 = re1.match(line)
        if m1:
            mask = m1.group(1)
            mask_op = int(mask.replace('X', '0'), 2)
            mask_mask = int(mask.replace('0', '1').replace('X', '0'), 2)

        m2 = re2.match(line)
        if m2:
            addr = int(m2.group(1))
            val = int(m2.group(2))

            val &= ~mask_mask
            val |= mask_op

            mem[addr] = val

    return sum(mem.values())


def part2(file):
    lines = [line.rstrip('\n') for line in open(file)]

    re1 = re.compile("^mask = (.*)$")
    re2 = re.compile("^mem\[(.*)\] = (.*)$")

    masks = []
    mask_mask = 0

    mem = {}

    for line in lines:
        m1 = re1.match(line)
        if m1:
            mask = m1.group(1)

            mask_mask = int(mask.replace('1', '0').replace('X', '1'), 2)

            masks = [mask]
            for i in range(len(mask)-1, -1, -1):
                if mask[i] == 'X':
                    masks = [m[:i] + '0' + m[i+1:] for m in masks] + [m[:i] + '1' + m[i+1:] for m in masks]

        m2 = re2.match(line)
        if m2:
            addr = int(m2.group(1))
            val = int(m2.group(2))

            for m in masks:
                decoded = (addr & ~mask_mask) | int(m, 2)
                mem[decoded] = val

    return sum(mem.values())


# Run

print("# Part 1")
print("- Test:", part1("day14/example.txt"), 165)
print("- Input:", part1("day14/input.txt"), 5902420735773)

print("# Part 2")
print("- Example:", part2("day14/example2.txt"), 208)
print("- Input:", part2("day14/input.txt"), 3801988250775)
