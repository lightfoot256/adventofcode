
import copy

def part1(file):
    lines = [line.rstrip('\n').split() for line in open(file)]

    ip = 0
    acc = 0
    count = {}

    while True:
        line = lines[ip]
        op = line[0]
        oa = int(line[1])

        print(ip, acc, op, oa)

        count[ip] = count.get(ip,0) + 1
        if count[ip] > 1:
            break

        if op == "acc":
            acc = acc + oa
            ip = ip + 1
        elif op == "jmp":
            ip = ip + oa
        elif op == "nop":
            ip = ip + 1

    return acc


def part2(file):
    lines = [line.rstrip('\n').split() for line in open(file)]

    versions = []
    linenum = 0

    # Original
    versions.append(copy.deepcopy(lines))

    for line in lines:

        if line[0] == "jmp":
            newversion = copy.deepcopy(lines)
            newversion[linenum][0] = "nop"
            versions.append(newversion)
        elif line[0] == "nop":
            newversion = copy.deepcopy(lines)
            newversion[linenum][0] = "jmp"
            versions.append(newversion)

        linenum = linenum + 1

    for version in versions:

        lines = version

        ip = 0
        acc = 0
        count = {}

        while True:

            print(ip)

            line = lines[ip]
            op = line[0]
            oa = int(line[1])

            #print(ip, acc, op, oa)

            count[ip] = count.get(ip, 0) + 1
            if count[ip] > 1:
                break

            if op == "acc":
                acc = acc + oa
                ip = ip + 1
            elif op == "jmp":
                ip = ip + oa
            elif op == "nop":
                ip = ip + 1

            if ip >= len(lines):
                return acc

    return -1


print("Part 1")
print("Test:", part1("day8/example.txt"))
print("Input:", part1("day8/input.txt", ))

print("Part 2")
print("Test:", part2("day8/example.txt"))
print("Input:", part2("day8/input.txt", ))
