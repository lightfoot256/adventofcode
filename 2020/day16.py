# Day 16

import re


def part1(file):
    whole = open(file, 'r').read()

    re_field = re.compile("^(.*): ([0-9]*)-([0-9]*) or ([0-9]*)-([0-9]*)$")

    records = whole.split('\n\n')
    raw_fields = records[0].split('\n')
    your = records[1].split('\n')[1]
    raw_nearbys = records[2].split('\n')[1:]

    fields = {}
    nearbys = []

    for field in raw_fields:
        matched = re_field.match(field)
        fields[matched.group(1)] = [
            (int(matched.group(2)), int(matched.group(3))),
            (int(matched.group(4)), int(matched.group(5)))
        ]

    for nearby in raw_nearbys:
        nearbys.append([int(value) for value in nearby.split(',') if value != ''])

    notValid = []

    for nearby in nearbys:
        for value in nearby:

            valid = False
            for field in fields:
                ranges = fields[field]
                for range in ranges:
                    if( range[0] <= value <= range[1] ):
                        valid = True

            if not valid:
                notValid.append(value)

    return sum(notValid)


def part2(file):
    whole = open(file, 'r').read()

    re_field = re.compile("^(.*): ([0-9]*)-([0-9]*) or ([0-9]*)-([0-9]*)$")

    records = whole.split('\n\n')
    raw_fields = records[0].split('\n')
    raw_your = records[1].split('\n')[1:]
    raw_nearbys = records[2].split('\n')[1:]

    fields = {}
    nearbys = []
    your = None

    for field in raw_fields:
        matched = re_field.match(field)
        fields[matched.group(1)] = [
            (int(matched.group(2)), int(matched.group(3))),
            (int(matched.group(4)), int(matched.group(5)))
        ]

    for your in raw_your:
        your = [int(value) for value in your.split(',') if value != '']
        nearbys.append(your)

    for nearby in raw_nearbys:
        nearbys.append([int(value) for value in nearby.split(',') if value != ''])

    print(fields)
    print(nearbys)

    validTickets = []

    for nearby in nearbys:

        ticket = {
            'values': nearby
        }

        valid = True
        for i, value in enumerate(nearby):

            for field in fields:
                ranges = fields[field]
                for range in ranges:
                    if range[0] <= value <= range[1]:
                        if not ticket.get(i, False):
                            ticket[i] = []
                        ticket[i].append(field)
                    else:
                        valid = False
        if not valid:
            validTickets.append(ticket)

    mapping = []

    for i, field in enumerate(fields):

        sets = []
        for v in validTickets:
            if v.get(i, -1) != -1:
                sets.append(set(v[i]))
        mapping.append((i, set.intersection(*sets)))

    sortred = sorted(mapping, key=lambda m: len(m[1]))
    final = {}
    found = []
    for m in sortred:
        remaining = [r for r in m[1] if r not in found]
        found = found + remaining
        final[m[0]] = remaining[0]

    for f in final:
        print(f, final[f])

    result = 1
    totals = []
    for f in final:
        if final[f].startswith('departure'):
            print(f, final[f])
            totals.append(your[f])
            result *= your[f]

    print(totals)
    print(result)

    return result

# Run

print("# Part 1")
print("- Test:", part1("day16/example.txt"), 71)
print("- Input:", part1("day16/input.txt"), 20091)

print("# Part 2")
print("- Example:", part2("day16/example2.txt"))
print("- Input:", part2("day16/input.txt"), 2325343130651)
