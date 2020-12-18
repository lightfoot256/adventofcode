# Day 15

def part1(str, turns):
    numbers = [int(n) for n in str.split(',')]

    history = {}
    spoken = []

    for i in range(0, len(numbers)):
        if history.get(numbers[i],None) is None:
            history[numbers[i]] = []
        history[numbers[i]].append(i+1)
        spoken.append(numbers[i])

    for turn in range(len(numbers)+1, turns+1):

        last = spoken[-1]

        if len(history[last]) == 1:
            speak = 0
        else:
            speak = history[last][-1] - history[last][-2]

        if history.get(speak,None) is None:
            history[speak] = []

        history[speak].append(turn)
        spoken.append(speak)

    return spoken[-1]

# Run


print("# Part 1")
print(" - Example", part1("0,3,6", 2020), 436)
print(" - Example", part1("1,3,2", 2020), 1)
print(" - Example", part1("2,1,3", 2020), 10)
print(" - Part1", part1("5,2,8,16,18,0,1", 2020), 517)

print("# Part 2")
print(" - Example", part1("0,3,6", 30000000), 175594)
print(" - Part2", part1("5,2,8,16,18,0,1", 30000000), 1047739)
