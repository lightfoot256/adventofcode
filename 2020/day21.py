# Day 21


def parse_data(file):
    mapping = {}
    foods = []

    for line in open(file, 'r').read().split('\n'):
        if "(contains" in line:
            ingredients_string, allergens_string = line.replace(')', '').split("(contains ")
        else:
            ingredients_string, allergens_string = line, ''

        ingredients = ingredients_string.split()
        foods.append(ingredients)
        allergens = allergens_string.split(', ')

        for allergen in allergens:
            if allergen not in mapping:
                mapping[allergen] = set(ingredients)
            else:
                mapping[allergen] = mapping[allergen].intersection(set(ingredients))

    done = False
    allergens = []
    while not done:
        done = True

        for allergen, possible_ingredients in mapping.items():
            if len(possible_ingredients) == 1:
                ingredient = list(possible_ingredients)[0]
                allergens.append(ingredient)

                # Does this ingredient appear in other mappings
                for allergen2 in mapping.keys():
                    if ingredient in mapping[allergen2] and allergen2 != allergen:

                        # Remove from others and keep going
                        mapping[allergen2].remove(ingredient)
                        done = False

    # print(foods)
    # print(mapping)
    # print(allergens)

    return foods, mapping, allergens

def part1(file):

    foods, mapping, allergens = parse_data(file)

    total = 0
    for food in foods:
        for ingredient in food:
            if ingredient not in allergens:
                total += 1
    return total


def part2(file):
    foods, mapping, allergens = parse_data(file)

    result = []
    arranged = sorted(mapping.items(), key=lambda x: x[0])
    for ingredient in arranged:
        if len(ingredient[1]):
            result.append(ingredient[1].pop())
    return ','.join(result)

# Run


print("# Part 1")
print("- Example:", part1("day21/example.txt"), '==', 5)
print("- Input:", part1("day21/input.txt"), '==', 2627)

print("# Part 2")
print("- Example:", part2("day21/example.txt"), '==', 'mxmxvkd,sqjhc,fvjkl')
print("- Input:", part2("day21/input.txt"), '==', 'hn,dgsdtj,kpksf,sjcvsr,bstzgn,kmmqmv,vkdxfj,bsfqgb')
