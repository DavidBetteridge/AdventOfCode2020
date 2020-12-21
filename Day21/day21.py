def read_file():
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

foods,  ingredients = read_file()

for food in foods:
    ingredientsInFood, allergensInFood = food
    for allergen in allergensInFood:
        for ingredient in ingredients:
            if not ingredient in ingredientsInFood:
                if allergen in ingredients[ingredient]:
                    ingredients[ingredient].remove(allergen)

result = 0
for ingredient in ingredients:
    if len(ingredients[ingredient]) == 0:
        for food in foods:
            ingredientsInFood, allergensInFood = food
            if ingredient in ingredientsInFood:
                result += 1
print(result)                
    