def grouping_dishes(dishes):
    groups = {}
    for d, *v in dishes:
        for x in v:
            groups.setdefault(x, []).append(d)
    ans = []
    for x in sorted(groups):
        if len(groups[x]) >= 2:
            ans.append([x] + sorted(groups[x]))
    return ans


if __name__ == '__main__':
    dishes = [
        ['Salad', 'Tomato', 'Cucumber', 'Salad', 'Sauce'],
        ['Pizza', 'Tomato', 'Sausage', 'Sauce', 'Dough'],
        ['Quesadilla', 'Chicken', 'Cheese', 'Sauce'],
        ['Sandwich', 'Salad', 'Bread', 'Tomato', 'Cheese']
    ]

    print(grouping_dishes(dishes))

    dishes2 = [
        ["Pasta", "Tomato Sauce", "Onions", "Garlic"],
        ["Chicken Curry", "Chicken", "Curry Sauce"],
        ["Fried Rice", "Rice", "Onions", "Nuts"],
        ["Salad", "Spinach", "Nuts"],
        ["Sandwich", "Cheese", "Bread"],
        ["Quesadilla", "Chicken", "Cheese"]
    ]
    print(grouping_dishes(dishes2))
