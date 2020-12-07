import re


def part1(filename):
    whole = open(filename, 'r').read()

    records = whole.split('\n\n')

    valid = 0

    for record in records:

        byr = "byr" in record
        iyr = "iyr" in record
        eyr = "eyr" in record
        hgt = "hgt" in record
        hcl = "hcl" in record
        ecl = "ecl" in record
        pid = "pid" in record
        cid = "cid" in record

        if( byr and iyr and eyr and hgt and hcl and ecl and pid):
            valid = valid + 1

        #print("record: ", record)
        #print("----")

    return valid

def byr_valid(byr):
    if byr is None: return False
    if len(byr) != 4: return False
    if not (1920 <= int(byr) <= 2002): return False
    return True

def iyr_valid(iyr):
    if iyr is None: return False
    if len(iyr) != 4: return False
    if not (2010 <= int(iyr) <= 2020): return False
    return True

def eyr_valid(eyr):
    if eyr is None: return False
    if len(eyr) != 4: return False
    if not (2020 <= int(eyr) <= 2030): return False
    return True

def hgt_valid(hgt):
    if hgt is None: return False
    hgt_cm = re.search("([0-9]*)cm", hgt)
    if hgt_cm:
        if (150 <= int(hgt_cm.group(1)) <= 193):
            return True
    hgt_in = re.search("([0-9]*)in", hgt)
    if hgt_in:
        if (59 <= int(hgt_in.group(1)) <= 76):
            return True
    return False

def hcl_valid(hcl):
    if hcl is None: return False
    if not re.match('#[0-9a-f]{6}', hcl): return False
    return True

def ecl_valid(ecl):
    if ecl is None: return False
    if not ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"): return False
    return True

def pid_valid(pid):
    if pid is None: return False
    if not re.match('^[0-9]{9,9}$', pid): return False
    return True

def cid_valid(cid):
    return True

def isvalid(record):
    byr = record.get('byr')
    iyr = record.get('iyr')
    eyr = record.get('eyr')
    hgt = record.get('hgt')
    hcl = record.get('hcl')
    ecl = record.get('ecl')
    pid = record.get('pid')
    cid = record.get('cid')

    if not byr_valid(byr): return False
    if not iyr_valid(iyr): return False
    if not eyr_valid(eyr): return False
    if not hgt_valid(hgt): return False
    if not hcl_valid(hcl): return False
    if not ecl_valid(ecl): return False
    if not pid_valid(pid): return False
    if not cid_valid(cid): return False

    return True

def part2(filename):
    whole = open(filename, 'r').read()
    records = whole.split('\n\n')
    valid = 0
    for record in records:
        props = record.split()
        dict = {}
        for prop in props:
            kvp = prop.split(':')
            dict[kvp[0]] = kvp[1]

        if isvalid(dict):
            print("Valid:", dict)
            valid = valid + 1
        else:
            print("Invalid:", dict)

    return valid

print("Part 1")
print("Test:", part1("day4/example.txt"), "Expected", 2)
print("Input:", part1("day4/input.txt"))

print("Part 2")
print("Test Answer:", part2("day4/example.txt"))
print("Invalid Answer:", part2("day4/invalid.txt"))
print("Valid Answer:", part2("day4/valid.txt"))

print("byr valid", byr_valid("2002") is True)
print("byr invalid", byr_valid("2003") is False)
print("hgt valid", hgt_valid("60in") is True)
print("hgt valid", hgt_valid("190cm") is True)
print("hgt invalid", hgt_valid("190in") is False)
print("hgt invalid", hgt_valid("190") is False)
print("hcl valid", hcl_valid("#123abc") is True)
print("hcl invalid", hcl_valid("#123abz") is False)
print("hcl invalid", hcl_valid("123abc") is False)
print("ecl valid", ecl_valid("brn") is True)
print("ecl invalid", ecl_valid("wat") is False)
print("pid valid", pid_valid("000000001") is True)
print("pid invalid", pid_valid("0123456789") is False)

print("Input Answer:", part2("day4/input.txt"))
