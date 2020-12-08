
from utils import *
import re

DAY = "2"


def part1(input):
    lines = input.split('\n')
    total = 0
    for line in lines:
        p = re.compile("([0-9]*)x([0-9]*)x([0-9]*)")
        m = p.match(line)
        if m:
            l = int(m.group(1))
            w = int(m.group(2))
            h = int(m.group(3))
            a = l * w
            b = w * h
            c = h * l
            s = 2 * a + 2 * b + 2 * c
            e = min([a, b, c])
            total += s + e
    return total


def part2(input):
    lines = input.split('\n')
    total = 0
    for line in lines:
        p = re.compile("([0-9]*)x([0-9]*)x([0-9]*)")
        m = p.match(line)
        if m:
            l = int(m.group(1))
            w = int(m.group(2))
            h = int(m.group(3))
            a = 2 * (l + w)
            b = 2 * (w + h)
            c = 2 * (h + l)
            e = min([a, b, c])
            total += e + l*w*h
    return total


validate(part1("2x3x4"), 58)
validate(part1("1x1x10"), 43)
solution("Part 1", DAY, part1)

validate(part2("2x3x4"), 34)
validate(part2("1x1x10"), 14)
solution("Part 2", DAY, part2)
