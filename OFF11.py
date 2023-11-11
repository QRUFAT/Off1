def read():
    cook_book = {}
    file = open(file="recipes.txt", encoding='utf-8', mode='r')
    while True:
        name = file.readline().strip()
        if not name:
            break
        number = int(file.readline().strip())
        ingredients = []
        for i in range(number):
            ingredient = {}
            line = file.readline().strip().split(' | ')

            ingredient["ingredient_name"] = line[0]
            ingredient["quantity"] = line[1]
            ingredient["measure"] = line[2]
            ingredients.append(ingredient)
        cook_book[name] = ingredients
        file.readline()
    return cook_book
print(read())

