# Day 19

import re


def resolve(rules, rule, maxdepth):

    if maxdepth == 0:
        return ''

    tokens = rules[rule]
    regex = []

    for token in tokens:
        if token[0] == '\"':
            regex.append(token[1:-1])
        elif token == '|':
            regex.append('|')
        else:
            regex.append(resolve(rules, token, maxdepth-1))

    return '(' + ''.join(regex) + ')'


def part1(file):
    rules_str, messages_str = open(file, 'r').read().split('\n\n')

    rules = {}
    for line in rules_str.split('\n'):
        rule, definition = line.split(':')
        rules[rule] = definition.split()

    r = re.compile('^' + resolve(rules, '0', 15) + '$')

    count = 0
    for message in messages_str.split('\n'):
        if r.match(message):
            count += 1

    return count


def part2(file):
    rules_str, messages_str = open(file, 'r').read().split('\n\n')

    rules = {}
    for line in rules_str.split('\n'):
        rule, definition = line.split(':')

        if rule == '8':
            definition = "42 | 42 8"
        if rule == '11':
            definition = "42 31 | 42 11 31"

        rules[rule] = definition.split()

    r = re.compile('^' + resolve(rules, '0', 15) + '$')

    count = 0
    for message in messages_str.split('\n'):
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
