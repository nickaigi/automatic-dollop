def grouping_dishes(dishes):
    meals = {}
    solution = []
    main_ingredients = []
    for dish in dishes:
        meals[dish[0]] = dish[1:]

    [[main_ingredients.append(ing) for ing in v if ing not in main_ingredients] for k,v in meals.items()]

    print(main_ingredients)

if __name__ == '__main__':
    dishes = [
        ['Salad', 'Tomato', 'Cucumber', 'Salad', 'Sauce'],
        ['Pizza', 'Tomato', 'Sausage', 'Sauce', 'Dough'],
        ['Quesadilla', 'Chicken', 'Cheese', 'Sauce'],
        ['Sandwich', 'Salad', 'Bread', 'Tomato', 'Cheese']
    ]

    grouping_dishes(dishes)
