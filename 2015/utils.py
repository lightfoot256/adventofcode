
def read(filename):
    return open(filename, 'r').read()

def validate(given, expected):
    print('# Validate ', given, expected, given == expected)

def solution(title, day, part):
    print('# ', title)
    file = read("data/" + day + "/input.txt")
    print(part(file))
    print()