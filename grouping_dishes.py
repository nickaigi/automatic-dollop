def grouping_dishes(dishes):
    meals = {}
    temp_solution = []
    solution = []
    main_ingredients = []
    for dish in dishes:
        meals[dish[0]] = dish[1:]

    [[main_ingredients.append(ing) for ing in v if ing not in main_ingredients] for k,v in meals.items()]
    for ing in sorted(main_ingredients, key=str.lower):
        temp = []
        temp.append(ing)
        for d in dishes:
            if ing in d[1:]:
                temp.append(d[0])
        if len(temp) >= 3:
            temp_solution.append(temp)

    for s in temp_solution:
        temp = []
        temp.append(s[0])
        [temp.append(_) for _ in sorted(s[1:], key=str.lower)]
        solution.append(temp)
    return solution

if __name__ == '__main__':
    dishes = [
        ['Salad', 'Tomato', 'Cucumber', 'Salad', 'Sauce'],
        ['Pizza', 'Tomato', 'Sausage', 'Sauce', 'Dough'],
        ['Quesadilla', 'Chicken', 'Cheese', 'Sauce'],
        ['Sandwich', 'Salad', 'Bread', 'Tomato', 'Cheese']
    ]

    print(grouping_dishes(dishes))
