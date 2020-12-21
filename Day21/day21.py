def read_file():
    """Returns a tuple of its lines (foods) and a dictionary of ingredients.  The dictionary is keyed
    by ingredient and each entry initially contains a list of all possible allergens."""
    allAllergens = set()
    allIngredients = set()
    foods = []

    lines = open('Day21/day21.txt').read().splitlines()
    for line in lines:
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split(' ')
        allergens = allergens.replace(')', '').split(', ')

        for allergen in allergens:
            allAllergens.add(allergen)

        for ingredient in ingredients:
            allIngredients.add(ingredient)

        foods.append((ingredients, allergens))

        ingredients = {}
        for ingredient in allIngredients:
            ingredients[ingredient] = list(allAllergens)

    return foods,  ingredients

def remove_impossible_allergens(foods, ingredients):
    """  Removes allergens from ingredients which can't possible contain the allergen."""
    for food in foods:
        ingredientsInFood, allergensInFood = food
        for allergen in allergensInFood:
            for ingredient in ingredients:
                if not ingredient in ingredientsInFood:
                    if allergen in ingredients[ingredient]:
                        ingredients[ingredient].remove(allergen)    


def resolve_remaining_allergens(ingredients):
    keepTrying = True
    while keepTrying:
        keepTrying = False
        for ingredient in ingredients:               
            if len(ingredients[ingredient]) == 1:
                allergen = ingredients[ingredient][0]
                for ingredient2 in ingredients:               
                    if ingredient != ingredient2:
                        if allergen in ingredients[ingredient2]:
                            ingredients[ingredient2].remove(allergen)
                            keepTrying = True                            

def part_one(foods, ingredient):
    result = 0
    for ingredient in ingredients:
        if len(ingredients[ingredient]) == 0:
            for food in foods:
                ingredientsInFood, _ = food
                if ingredient in ingredientsInFood:
                    result += 1
    return result

def part_two(ingredients):
    allergens = []
    for ingredient in ingredients:               
        if len(ingredients[ingredient]) == 1:
            allergens.append((ingredients[ingredient][0], ingredient))

    return ','.join([a[1] for a in sorted(allergens)])

foods,  ingredients = read_file()
remove_impossible_allergens(foods,  ingredients)
resolve_remaining_allergens(ingredients)

print(part_one(foods, ingredients))
print(part_two(ingredients))

