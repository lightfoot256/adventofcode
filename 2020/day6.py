
def part1(file):
    whole = open(file, 'r').read()
    records = whole.split('\n\n')

    valid = 0
    for record in records:
        clean = ''.join(record.split())
        valid = valid + len(set(clean))

    return valid

def part2(file):
    whole = open(file, 'r').read()
    records = whole.split('\n\n')

    valid = 0
    for record in records:

        lines = record.split('\n')
        all = []

        for line in lines:
            all.append(set(line))

        if len(all) > 1:
            rcount = len(set.intersection(*all))
        else:
            rcount = len(all[0])

        valid = valid + rcount

    return valid

print("Part 1")
print("Test:", part1("day6/example.txt"))
print("Input:", part1("day6/input.txt"))

print("Part 2")
print("Test Answer:", part2("day6/example.txt"))
print("Input Answer:", part2("day6/input.txt"))

# 3431 too low
# 3445; line at the end of the file causing an issue :D