# Day 19

import regex

def resolve(lookup, rule, maxdepth):

    if maxdepth == 0:
        return ''

    parts = lookup[rule]

    foundOr = False
    result = []

    for p in parts:
        if p.isnumeric():
            result.append(resolve(lookup, int(p), maxdepth-1))
        elif p == '|':
            foundOr = True
            result.append('|')
        elif p[0] == '\"':
            result.append(p[1:-1])

    if foundOr:
        return '(' + ''.join(result) + ')'
    else:
        return ''.join(result)


def part1(file):
    whole = open(file, 'r').read()

    records = whole.split('\n\n')
    rules = records[0].split('\n')
    messages = records[1].split('\n')

    rlookup = {}

    for line in rules:
        parts = line.split(':')
        rule = int(parts[0])
        defn = parts[1]

        rlookup[rule] = defn.split()

    pattern = '^' + resolve(rlookup, 0, 50) + '$'

    r = regex.compile(pattern)

    count = 0
    for message in messages:
        if r.match(message):
            count += 1

    return count


def part2(file):
    whole = open(file, 'r').read()

    records = whole.split('\n\n')
    rules = records[0].split('\n')
    messages = records[1].split('\n')

    rlookup = {}

    for line in rules:
        parts = line.split(':')
        rule = int(parts[0])
        defn = parts[1]

        if rule == 8:
            defn = "42 | 42 8"
        if rule == 11:
            defn = "42 31 | 42 11 31"

        rlookup[rule] = defn.split()

    pattern = '^' + resolve(rlookup, 0, 50) + '$'

    r = regex.compile(pattern)

    count = 0
    for message in messages:
        if r.match(message):
            count += 1

    return count

# Run


print("# Part 1")
print("- Example:", part1("day19/example.txt"), 2)
print("- Input:", part1("day19/input.txt"), 180)

print("# Part 2")
print("- Example:", part2("day19/example2.txt"), 12)
print("- Input:", part2("day19/input.txt"), 323)
