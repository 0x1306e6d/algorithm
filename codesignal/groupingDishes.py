def solution(dishes):
    ingredients = {}
    for dish in dishes:
        name = dish[0]
        for ingredient in dish[1:]:
            if ingredient not in ingredients:
                ingredients[ingredient] = []
            ingredients[ingredient].append(name)
    arr = []
    for ingredient in sorted(ingredients):
        if len(ingredients[ingredient]) >= 2:
            arr.append([ingredient] + list(sorted(ingredients[ingredient])))
    return arr
