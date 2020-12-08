
import re

def getRules(file):

    p = re.compile("^(.*) bags contain (.*).$")
    p2 = re.compile("([0-9]*) (.*) bags?")
    lines = [line.rstrip('\n') for line in open(file)]

    rules = {}

    for line in lines:
        r = p.match(line)
        if r:
            contains = r.group(2).split(', ')
            for contain in contains:
                r2 = p2.match(contain)
                if r2:
                    if(rules.get(r.group(1)) is None):
                        rules[r.group(1)] = []
                    rules[r.group(1)].append( (r2.group(1), r2.group(2)) )
                elif contain == "no other bags":
                    rules[r.group(1)] = []

    for rule in rules:
        print(rule, ":", rules[rule])

    return rules


def part1(file):

    rules = getRules(file)
    lookingfor = "shiny gold"
    foundin = {}

    tocheck = []
    for rule in rules:
        for rulecontain in rules[rule]:
            if rulecontain[1] == lookingfor:
                foundin[rule] = rules[rule]
                tocheck.append(rule)

    while len(tocheck):
        check = tocheck.pop()
        for rule in rules:
            for rulecontain in rules[rule]:
                if rulecontain[1] == check:
                    foundin[rule] = rules[rule]
                    tocheck.append(rule)

    valid = len(foundin)
    return valid

def part2(file):

    rules = getRules(file)
    lookingfor = "shiny gold"
    bags = 0

    tocheck = []
    for rule in rules:
        if rule == lookingfor:
            for c in rules[rule]:
                tocheck.append(c)

    while len(tocheck):
        check = tocheck.pop()
        multiplier = int(check[0])
        bags += multiplier
        for rule in rules:
            if rule == check[1]:
                for c in rules[rule]:
                    tocheck.append((
                        int(c[0]) * multiplier,
                        c[1]
                    ))

    return bags


print("Part 1")
print("Test:", part1("day7/example.txt"), 4)
print("Input:", part1("day7/input.txt"))

print("Part 2")
print("Test Answer:", part2("day7/example.txt"), 32)
print("Example2 Answer:", part2("day7/example2.txt"), 126)

print("Input Answer:", part2("day7/input.txt"))
