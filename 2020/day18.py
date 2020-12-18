# Day 18

import re


def resolve_brackets(string, promote_addition):

    stack = [[]]
    for char in string:
        if char == '(':
            stack.append([])
        elif char == ')':
            sub = str(resolve_expr(''.join(stack.pop()), promote_addition))
            if len(stack):
                stack[-1].append(sub)
            else:
                return sub
        else:
            stack[-1].append(char)

    return ''.join(stack[0])


def resolve_additions(string):
    while '+' in string:
        string = re.sub('([0-9]{1,}) \+ ([0-9]{1,})', lambda m: str(int(m.group(1)) + int(m.group(2))), string)
    return string


def resolve_expr(string, promote_addition):

    if '(' in string:
        string = resolve_brackets(string, promote_addition)

    if promote_addition:
        string = resolve_additions(string)

    parts = string.split(' ')

    total, i = 0, 0
    while i < len(parts):
        op = parts[i+0]

        if op.isnumeric():
            total = int(op)
            i += 1
        else:
            oa = int(parts[i + 1])
            i += 2

            if op == '+':
                total += oa
            if op == '*':
                total *= oa

    return total


def part1(file):
    lines = [line.rstrip('\n') for line in open(file)]

    total = 0
    for line in lines:
        total += resolve_expr(line, False)

    return total


def part2(file):
    lines = [line.rstrip('\n') for line in open(file)]

    total = 0
    for line in lines:
        total += resolve_expr(line, True)

    return total

# Run


print("# Part 1")
print("- Test:", part1("day18/example.txt"), 71)
print("- Test:", part1("day18/example2.txt"), 51)
print("- Test:", part1("day18/example3.txt"), 26)
print("- Input:", part1("day18/input.txt"), 7293529867931)

print("# Part 2")
print("- Example:", part2("day18/example4.txt"), 231)
print("- Input:", part2("day18/input.txt"), 60807587180737)
