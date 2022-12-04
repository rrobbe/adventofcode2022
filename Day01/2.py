input_data = [line.strip() for line in open('input', 'r')]
top_n = 3


def get_top_n_calories(inventory, n):
    elfs = []
    calories = 0

    for calorie in inventory:
        if calorie == "":
            elfs.append(calories)
            calories = 0
        else:
            calories += int(calorie)
    return sum(sorted(elfs, reverse=True)[:n])


print(get_top_n_calories(input_data, top_n))


