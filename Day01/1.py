input_data = [line.strip() for line in open('input', 'r')]


def get_max_calories(inventory):
    elfs = []
    calories = 0

    for calorie in inventory:
        if calorie == "":
            elfs.append(calories)
            calories = 0
        else:
            calories += int(calorie)
    return max(elfs)


print(get_max_calories(input_data))

